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
from typing import NamedTuple, Union, Tuple

from CRRD.defs import *
from CRRD.trainno import resolveTrainNo
from CRRD.utils import hex2bcd, decimal2mileage, bytes2hex


class LBJ821Notice(NamedTuple):
    train_no: int
    speed: Union[int, None]
    mileage: Union[Decimal, None]


class LBJ821Time(NamedTuple):
    time: datetime.time


class LBJ866GroundAlarm:
    """
    TB/T3504-2008 p.14-p.15
    地面设备：道口事故报警信息、施工防护报警信息
    """

    def __init__(self, packed_data: bytes):
        data = struct.unpack("<B3sIB8s", packed_data)
        self.function: str = lbj_func.get(data[0])
        self.mileage: Decimal = self.parse_mileage(data[1])
        self.send_time: datetime.datetime = self.parse_time(data[2])
        if data[3] != 0xff:
            self.reason: str = lbj_alarm_cleared_reason_trans.get(data[3], '未知原因')
        else:
            self.reason = None
        self.line_name: str = data[4].decode('GBK')  # Untested!

    @staticmethod
    def parse_time(t: int) -> datetime.datetime:
        s = (t >> 0) & 0x3f  # 6
        m = (t >> 6) & 0x3f  # 6
        h = (t >> 12) & 0x1f  # 5
        d = (t >> 17) & 0x1f  # 5
        M = (t >> 22) & 0xf  # 4
        y = (t >> 26) & 0x3f  # 6
        return datetime.datetime(year=2000 + y, month=M, day=d, hour=h, minute=m, second=s)

    @staticmethod
    def parse_mileage(b: bytes) -> Decimal:
        tmp = int.from_bytes(b, 'little')
        mileage = tmp & 0x3fffff
        if tmp & (1 << 22):
            mileage = -mileage
        return Decimal("%.3f" % (mileage / 1000))

    @staticmethod
    def decode_text(b: bytes) -> str:
        raise NotImplementedError("We hasn't receive such package yet, please report")

    def to_string(self) -> str:
        pass


class LBJ866TrainAlarm:
    """
    车载设备：列车防护报警信息
    """

    def __init__(self, packed_data: bytes):
        data = struct.unpack("<B4s3s4s3s4sB", packed_data)
        self.function: str = lbj_func.get(data[0])
        self.train_no_header: str = data[1].decode('ascii')
        self.train_no: int = int.from_bytes(data[2], 'little')
        self.locomotive_no: int = int(hex2bcd(data[3]))
        self.mileage: Decimal = LBJ866GroundAlarm.parse_mileage(data[4])
        self.send_time: datetime.datetime = LBJ866GroundAlarm.parse_time(data[5])
        self.alarm_source: str = lbj_alarm_source_trans.get(data[6], '未知')

    def to_string(self) -> str:
        pass


class LBJ866Test:
    def __init__(self, packed_data: bytes):
        data = struct.unpack("<B4s", packed_data[:5])
        self.function: str = lbj_func.get(data[0])
        self.locomotive_no: int = int(hex2bcd(data[3]))
        if len(packed_data) > 5:
            data2 = struct.unpack("3B", packed_data[5:])
            self.control_port = lbj_test_port_trans.get(data2[0])
            self.test_result = data2[1]
            self.battery_voltage = Decimal("%.1f" % (data2[2] / 10))
        else:
            self.control_port = None
            self.test_result = None
            self.battery_voltage = None

    def to_string(self) -> str:
        pass


class LW:
    def __init__(self, packed_data: bytes):
        length = len(packed_data)
        self.clock_sync = None
        self.lw_id = None
        if length == 6:
            data = struct.unpack("2s2s2s", packed_data)
            self._parse(data)
        elif length == 11:
            """
            KLW (loco. no length = 8)
            ... 24 00 04 23 | 00 91 | 20 07 78 | ff ff | d6 29
            ...   loco no      cmd     KLW ID    param    crc
            decoded example: Locomotive 240-0423, Query pressure(cmd=0x91) from KLW 200778
            """
            data = struct.unpack("2s2s2s3s2s", packed_data)
            if data[3] == b'\xaa\xaa\xa0':
                # Exception: 450MHz LW over 800MHz channel
                # refer to LBJ兼容货尾方案(讨论稿)―按铁科意见修改-11 0603
                self._parse(data[:3])
            else:
                self._parse((data[0] + data[1], data[2], data[4]))
                self.lw_id = hex2bcd(data[3])
        elif length == 15:
            """
            LW
            ... 60 41 | a5 91 | 13 21 | 32 | 23 70 | 13 21 | 22 16 14 00 | 6a 50
            ... loco1    cmd    param   lw1  loco2    lw2      unknown      crc
            decode example: Locomotive 237-6041, Query pressure(cmd=0x91) from LW 321321
            """
            data = struct.unpack("2s2s2sc2s2s4s", packed_data)
            self._parse((data[4] + data[0], data[1], data[2], data[6]))
            self.lw_id = hex2bcd(data[3] + data[5])
        elif length == 17 and packed_data[5] in [0xa1, 0xa2]:
            # KLW with clock sync
            data = struct.unpack("2s2s2s3s2s6s", packed_data)
            self._parse((data[0] + data[1], data[2], data[4]))
            self.lw_id = hex2bcd(data[3])
            self.clock_sync = datetime.datetime.strptime(hex2bcd(data[5]), '%y%m%d%H%M%S')
        else:
            raise RuntimeError(f"Unknown LW package {packed_data}")

    def _parse(self, data: Tuple):
        loco_no = hex2bcd(data[0])
        self.locomotive_model = loco_model_trans.get(int(loco_no[:3]), loco_no[:3])
        self.locomotive_no = loco_no[4:]
        self.cmd_reserved = data[1][0]
        self.cmd = lw_cmd.get(data[1][1], f'未知指令{hex(data[1][1])}')
        self.param = hex2bcd(data[2])
        self.more = data[3:]

    def to_string(self) -> str:
        if self.param in ['[[?5', '[[[[']:  # invalid param
            param = ''
        else:
            param = self.param

        if self.clock_sync:
            clock = f'时间:{self.clock_sync}'
        else:
            clock = ''

        if self.lw_id:
            lw_id = f'{self.lw_id}列尾'
        else:
            lw_id = ''

        if self.more:  # Not documented on references
            more = f'(more=0x{bytes2hex(self.more[0])})'
        else:
            more = ''

        return f"{self.locomotive_model}-{self.locomotive_no}机车 {lw_id} {self.cmd} {param} {clock} {more}"


class CIR450TrainNo:
    def __init__(self, packed_data: bytes):
        data = struct.unpack("<3B4s3s2BH3s3s2H5B3s", packed_data)
        self.dmis_semaphore: int = dmis_semphore_trans.get(data[0], '未知')
        self.semaphore_type: int = dmis_semphore_trans.get(data[1], '未知')
        self.locomotive_type: int = loco_type_trans.get(data[2] & 0x3)
        self.train_no_header: str = data[3].decode('ascii')
        self.train_no: int = int.from_bytes(data[4], 'little')
        self.locomotive_model: int = loco_model_trans.get(data[5], data[5])
        self.locomotive_model_ext: int = data[6]
        self.locomotive_no: int = data[7]
        self.direction, self.mileage, self.is_test = CIR450TrainNo._covert_mileage(data[8])
        self.reserved_1, self.train_speed = CIR450TrainNo._covert_speed(data[9])
        self.train_weight: int = data[10]
        self.train_length: Decimal = Decimal("%.1f" % (data[11] / 10))
        self.train_carriages: int = data[12]
        self.station_no: int = data[13]
        self.station_no_ext: int = data[14]
        self.segment_no: int = data[15]
        self.segment_no_actual: int = data[16]
        self.driver_id: int = int.from_bytes(data[17], 'little')

        self.full_train_no: str = self.train_no_header.strip() + str(self.train_no)

    def __repr__(self):
        return f'CIR450TrainNo(train_no={self.full_train_no}, speed={self.train_speed}, mileage={self.mileage})'

    @staticmethod
    def _covert_mileage(b: bytes) -> Tuple[Union[bool, None], Union[Decimal, None], int]:
        tmp = int.from_bytes(b, 'little')
        direction = None
        mileage = None
        is_test = False
        if tmp in [9999888, 8888888]:  # This is test data
            is_test = True
        elif tmp in [0xffffff, 9999999]:  # Mileage is unknown
            pass
        else:
            mileage = Decimal("%.3f" % ((tmp & 0x3fffff) / 1000))
            if tmp & (1 << 23):
                mileage = -mileage
            direction = int(bool((tmp & (1 << 22))))
        return direction, mileage, is_test

    @staticmethod
    def _covert_speed(b: bytes) -> Tuple[int, int]:
        tmp = int.from_bytes(b, 'little')
        speed = tmp & 0x3ff
        reserved = tmp >> 10
        return reserved, speed

    def to_string(self) -> str:
        dmis_semaphore = self.dmis_semaphore
        loco_type = self.locomotive_type
        locomotive = "%s-%04d" % (self.locomotive_model, self.locomotive_no)
        train_property = '总重: %dt 辆数:%d 计长:%s' % (self.train_weight, self.train_carriages, self.train_length)

        # Mileage
        if self.direction is None:
            direction = '(x)'
        else:
            direction = '(+)' if self.direction else '(-)'
        if self.mileage is None:
            train_mileage = '公里标：未知'
        else:
            if self.mileage < 0:
                sign = '-'
                mileage = abs(self.mileage)
            else:
                sign = ''
                mileage = self.mileage
            train_mileage = '公里标：%s%s' % (sign, decimal2mileage(mileage)) + direction

        # Train No 
        train_no = self.full_train_no
        try:
            _, _, train_no_desc, train_no_relegation = resolveTrainNo(train_no)
        except ValueError:
            train_no_desc = '无效车次'
            train_no_relegation = None
        if train_no_relegation is None:
            train_no_relegation = ''
        train_speed = '速度：%dkm/h' % self.train_speed
        segment = '区段号:' + str(self.segment_no) + ' ' + str(self.segment_no_actual)
        driver = '司机号:' + str(self.driver_id)
        station = '车站号:' + str(self.station_no)

        info = ' '.join((loco_type, locomotive, '担当%s次 %s%s' % (train_no, train_no_relegation, train_no_desc),
                         train_mileage, train_speed, train_property, segment, driver, station, dmis_semaphore))
        if self.is_test:
            info += '(测试数据)'

        return info


class CIR450DispatchCommand:
    def __init__(self, packed_data: bytes):
        data, text = struct.unpack("1B3s3s3s7s8s1B6s8s1s5s2B", packed_data[:48]), self.decode_text(packed_data[48:])
        self.function = dispatch_cmd_func.get(data[0], default='未知功能')
        self.datetime = datetime.datetime.strptime(hex2bcd(data[1] + data[2]), '%y%m%d%H%M%S')
        self.relay_time = datetime.time.strftime(hex2bcd(data[3]), '%H%M%S')
        self.train_no = data[4].decode('ascii')
        self.loco_no = data[5].decode('ascii')
        self.dispatch_no = data[6]
        self.command_no = data[7].decode('ascii')
        self.dispatcher_name = self.decode_text(data[8])
        self.state = 0x00  # always transmitted as 0x00
        self.reserved = data[10]
        self.package_amount = data[11]
        self.package_no = data[12]

    @staticmethod
    def decode_text(barr: bytes) -> str:
        raise NotImplementedError("We hasn't receive such package yet, please report")

    def to_string(self) -> str:
        pass


class CIR450DispatchCommandReply:
    def __init__(self, packed_data: bytes):
        data = struct.unpack("2B3s3s7s8sB6s3s5s4s5sB", packed_data)
        self.name: str = dispatch_reply_name_trans.get(data[0], '待定')
        self.function: str = dispatch_cmd_func.get(data[1], '未知功能')
        self.datetime: datetime.datetime = datetime.datetime.strptime(hex2bcd(data[2] + data[3]), '%y%m%d%H%M%S')
        self.full_train_no = data[4].decode('ascii').strip()
        if self.full_train_no == 'XXXXXXX':
            self.full_train_no = None
        self.loco_no = data[5].decode('ascii').strip()  # need more received package to verify this field
        self.dispatch_no: int = data[6]
        self.command_no: str = data[7].decode('ascii')
        self.mileage: Decimal = self._parse_mileage(data[8])
        self.gps = self._parse_gps(hex2bcd(data[9]), hex2bcd(data[10]))
        self.reserved: int = data[11]
        self.package_no: int = data[12]

    def __repr__(self):
        return f'CIR450DispatchCommandReply(train_no={self.full_train_no}, name={self.name}, function={self.function})'

    @staticmethod
    def _parse_gps(latitude: str, longitude: str) -> Union[None, Tuple[Decimal, Decimal]]:
        if latitude.isdigit() and longitude.isdigit():
            return Decimal(latitude[:4] + '.' + latitude[4:]), Decimal(longitude[:2] + '.' + longitude[2:])
        else:
            return None

    @staticmethod
    def _parse_mileage(b: bytes) -> Union[None, Decimal]:
        val = int.from_bytes(b, 'little')
        if val in [0xffffff, 9999999]:
            return None
        else:
            return Decimal("%.3f" % val)

    def to_string(self) -> str:
        if self.full_train_no is not None:
            train = f'{self.full_train_no}次机车{self.loco_no}'
        else:
            train = f'{self.loco_no}机车'

        if self.name in ['请求调车', '请求入库检']:
            action = self.name
            package_no = f'包号:{self.package_no}'
            dispatch = f''
        else:
            action = f"{self.function}{self.name}"
            package_no = f'总包数:{self.package_no}'
            dispatch = f'调度所:{self.dispatch_no} 命令号:{self.command_no}'

        if self.gps is None:
            gps = 'GPS:未知'
        else:
            gps = f'GPS:{self.gps[0]}E {self.gps[1]}N'
        if self.mileage is None:
            mileage = '公里标：未知'
        else:
            mileage = '公里标：%s' % (decimal2mileage(self.mileage))

        return f'{train}{action}于 {gps} {mileage} 时间:{self.datetime} {dispatch} {package_no} '


class FFSKHeader(NamedTuple):
    mode_word: int
    data_length: int
    address: bytes
    control_word: int
    command_word: int
    function_code: int
    payload_length: int
