# MIT License
#
# Copyright (c) 2020 Alex L Manstein (alex.l.manstein@gmail.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import datetime
import struct
from decimal import Decimal
from typing import List, Tuple, Union, Any

from CRRD.package import FFSKHeader, CIR450TDCS, LBJ821Notice, CIR450LW, LBJ821Time
from CRRD.utils import crc16, hex2bcd


class UnknownPackage(ValueError):
    pass


class BrokenPackage(ValueError):
    pass


class EmptyPackage(ValueError):
    pass


class POCSAGDecoder:
    """
    Refer to TB∕T3504-2018 "Train approaching alarm ground equipment"
    """

    @staticmethod
    def decode(package_text: str, address: int) -> Tuple[str, Any]:
        """
        parse POCSAG text to LBJ alarm or LBJ time messages
        :param package_text: received POCSAG text
        :param address: address *without* function code
        :return:
        """
        if isinstance(package_text, str):
            package = tuple(filter(lambda x: x, package_text.strip().split(" ")))
            if POCSAGDecoder.validate(package, address):
                if address == 1234000:
                    train_no, speed, mileage = map(POCSAGDecoder._parse_notice_segment, package)
                    if train_no or mileage:
                        if mileage:
                            return LBJ821Notice._make((train_no, speed, Decimal("%.1f" % (mileage / 10))))
                        else:
                            return LBJ821Notice._make((train_no, speed, None))
                    else:
                        raise EmptyPackage
                elif address == 1234008:
                    return LBJ821Time._make((POCSAGDecoder._parse_time(package[0]),))
        else:
            raise ValueError(f"Invalid type {type(package_text)} for package text")

    @staticmethod
    def _parse_notice_segment(s: str) -> Union[None, int]:
        if '-' in s:
            return None
        else:
            return int(s)

    @staticmethod
    def _parse_time(s: str) -> datetime.time:
        return datetime.time(hour=int(s[1:3]), minute=int(s[3:5]))

    @staticmethod
    def validate(package: List[str], address: int) -> bool:
        """
        Validate LBJ POCSAG packages
        :param package: text of package
        :param address: POCSAG address of this package
        :return:

        POCSAG has no CRC validation thus received data could be erroneous (including address)

        821MHz LBJ Alarm (address = 1234000) Example:
        Valid ones:
        1328 294 11761: Train 1328, speed 294kph, mileage K1176+100m
        86052 5 ----- : Mileage unknown
        ----- --- ----- : Totally unknown (often marshalling loco.)
        ----- 5 ----- : Only speed is known

        Invalid ones:
        10808 87 1[7. : POCSAG BCH decoding error
        10835 43 11695828-1 : overlap with other transmission

        We may need extra methods to prevent pseudo valid ones say error happened
        but looked fine however make no sense in the context

        821MHz LBJ Time (address = 1234008) Example:
        *0302 : 3 o'clock and 2 minutes, localtime
          '*' stands for any non-digit char, depends on POCSAG decoder's charset (value 0xA)

        """
        if address == 1234000:  # LBJ alarm
            if len(package) != 3:
                raise BrokenPackage
            unknown_fill = ['-----', '---', '-----']
            for i in range(3):
                if package[i].isdigit() and len(package[i]) <= len(unknown_fill[i]) or package[i] == unknown_fill[i]:
                    continue
                else:
                    raise BrokenPackage
            return True
        elif address == 1234008:  # LBJ time
            if len(package) != 1 and len(package[0]) != 5:
                raise BrokenPackage
            text = package[0]
            if not text[0].isdigit() and text[1:].isdigit() and int(text[1:3]) < 24 and int(text[3:5]) < 60:
                return True
            raise BrokenPackage
        else:
            raise UnknownPackage


class FFSKDecoder(object):
    """
    reference: TB/T 3052-2002


    """

    def __init__(self, packageData, ignoreCrc=True):
        pass

    @staticmethod
    def decode(package_bytes: bytes):
        header = FFSKHeader._make(struct.unpack(">2B5s4B", package_bytes[:11]))
        payload = package_bytes[11:-2]
        crc = struct.unpack(">H", package_bytes[-2:])[0]
        if len(payload) != header.payload_length or crc != crc16(package_bytes[:-2]):
            # raise BrokenPackage
            print('broken!')
            return None
        if header.address == b'\x00\x3f\x1f\x00\x00' and \
                header.control_word == 0x1f and \
                header.command_word == 0x8c and \
                header.function_code == 0x30:
            # This is TDCS Wireless train no package
            if len(payload) != 32:
                raise BrokenPackage
            package = CIR450TDCS._make(payload)
            # TODO: Add validation here
            print(package.to_string())
            return package
        elif (header.address == b'\x41\x3f\x1f\x00\x00' or
              header.address == b'\x41\x3f\x1f\x00\x01') and \
                header.mode_word == 0x0c and \
                header.control_word == 0x1f and \
                header.command_word == 0x8c and \
                header.function_code == 0xa5:
            # This is LW system package, TODO: Support different standards of LW
            if len(payload) == 15:
                locomotive_no = hex2bcd(payload[0:2])
                command = payload[2:4]
                param = payload[4:6]
                more = payload[6:]
                package = CIR450LW._make((locomotive_no, command, param, more))
        elif header.address == b'\x00\x00\x00\x00\x00' and \
                header.mode_word == 0x0c and \
                header.control_word == 0x1f and \
                header.command_word == 0x8c and \
                header.function_code == 0x40:
            """
            Reference:
            TB/T 3504-2018 - 道口报警、施工防护报警
            800MHz旅客列车尾部装置和列车防护报警系统设备技术条件(讨论稿20090903)
            """
            pass  # TODO: Support TB/T 3504-2018
        else:
            print('Unknown!')
            raise UnknownPackage
