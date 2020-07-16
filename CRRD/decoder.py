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

from CRRD.package import *
from CRRD.utils import crc16


# TODO: do validation when decoding packages, to distinct broken or unknown packages
class UnknownPackage(ValueError):
    pass


class BrokenPackage(ValueError):
    pass


class EmptyPackage(ValueError):
    pass


class POCSAGDecoder:
    """
    Reference: TB∕T3504-2018《列车接近预警地面设备》（列车接近预警部分）
    """

    @staticmethod
    def decode(package_text: str, address: int) -> Union[LBJ821Notice, LBJ821Time]:
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
                        raise EmptyPackage("Empty Package")
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
    def validate(package: Tuple[str], address: int) -> bool:
        """
        Validate LBJ POCSAG packages
        :param package: text of package
        :param address: POCSAG address of this package
        :return: bool: is valid or not

        POCSAG has no CRC validation thus received data could be erroneous (including address)

        1. 821MHz LBJ Alarm (address = 1234000) Example:
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

        2. 821MHz LBJ Time (address = 1234008) Example:
        *0302 : 3 o'clock and 2 minutes, localtime
          '*' stands for any non-digit char, depends on POCSAG decoder's charset (value 0xA)

        """
        if address == 1234000:  # LBJ alarm
            if len(package) != 3:
                raise BrokenPackage("Broken Package: Invalid format")
            unknown_fill = ['-----', '---', '-----']
            for i in range(3):
                if package[i].isdigit() and len(package[i]) <= len(unknown_fill[i]) or package[i] == unknown_fill[i]:
                    continue
                else:
                    raise BrokenPackage(f"Broken Package: Part{i + 1}")
            return True
        elif address == 1234008:  # LBJ time
            if len(package) != 1 and len(package[0]) != 5:
                raise BrokenPackage("Broken Package: Invalid format")
            text = package[0]
            if not text[0].isdigit() and text[1:].isdigit() and int(text[1:3]) < 24 and int(text[3:5]) < 60:
                return True
            raise BrokenPackage("Broken Package: Invalid time")
        else:
            raise UnknownPackage


class FFSKDecoder(object):
    """
    reference: TB/T 3052-2002《列车无线调度通信系统制式及主要技术条件》
    """

    @staticmethod
    def decode(package_bytes: bytes):
        header = FFSKHeader._make(struct.unpack(">2B5s4B", package_bytes[:11]))
        payload = package_bytes[11:-2]
        crc = struct.unpack(">H", package_bytes[-2:])[0]
        if len(payload) != header.payload_length or crc != crc16(package_bytes[:-2]):
            print('broken!')
            raise BrokenPackage
        if header.address == b'\x00\x3f\x1f\x00\x00' and \
                header.control_word == 0x1f and \
                header.command_word == 0x8c:
            if header.function_code == 0x30:
                """
                TDCS wireless train no package
                References:
                1. GSM-R数字移动通信应用技术条件 第二分册：列车无线车次号校核信息传输系统(V1.0) [2007.3]
                2. TB/T 3325—2013《列车无线车次号校核信息传送系统》
                """
                if len(payload) != 32:
                    raise BrokenPackage
                package = CIR450TrainNo(payload)
                # TODO: Add validation here
                if package.locomotive_model == 0 or package.train_no == 0 or len(str(package.driver_id)) < 7:
                    raise EmptyPackage
                return package

            elif header.function_code == 0x88:
                """
                TDSC wireless dispatch command package
                References:
                1. 450MHz 调度命令无线传输系统技术条件(V.43) [铁道部运输局 2005.4]
                THIS IS PARTLY UNTESTED!! NO PACKAGE RECEIVED FOR VERIFICATION
                """
                if payload[0] in [0x80, 0x81, 0x82, 0x91]:  # Locomotive -> Station
                    package = CIR450DispatchCommandReply(payload)
                    return package
                elif 1 <= payload[0] <= 0x20:  # Station -> Locomotive
                    package = CIR450DispatchCommand(payload)
                    return package

        elif (header.address == b'\x41\x3f\x1f\x00\x00' or
              header.address == b'\x41\x3f\x1f\x00\x01') and \
                header.mode_word == 0x0c and \
                header.control_word == 0x1f and \
                header.command_word == 0x8c and \
                header.function_code == 0xa5:
            """
            LW system package (LW: train tail device, used for monitoring pipe pressure, may on various channels)
            Reference:
            1. TB/T 2973-2006 《列车尾部安全防护装置及附属设备》 (FFSK over 450MHz channel)
            2. TJ/DW 012—2009《列车防护报警和客车列尾系统技术条件》（FFSK over 800MHz channel)
            TBD: GSM-R channel, DMR over 400MHz channel
            """
            try:
                package = LW(payload)
                return package
            except RuntimeError as Error:
                raise UnknownPackage(str(Error))

        elif header.address == b'\x00\x00\x00\x00\x00' and \
                header.mode_word == 0x0c and \
                header.control_word == 0x1f and \
                header.command_word == 0x8c and \
                header.function_code == 0x40:
            """
            Train protection alarm package
            References:
            1. TB/T 3504-2018《列车接近预警地面设备》（道口报警、施工防护报警部分）
            2. TJ/DW 012—2009《列车防护报警和客车列尾系统技术条件》
            THIS IS UNTESTED!! NO PACKAGE RECEIVED FOR VERIFICATION
            """
            function = payload[0]
            if function in (1, 2):
                package = LBJ866TrainAlarm(payload)
            elif function in (3, 4, 5, 6):
                package = LBJ866GroundAlarm(payload)
            elif function in (7, 8):
                package = LBJ866Test(payload)
            else:
                raise UnknownPackage(f"Invalid function {function} for train protection alarm package")
            return package

        else:
            print('Unknown!')
            raise UnknownPackage
