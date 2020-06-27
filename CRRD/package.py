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


class LBJ821Notice(NamedTuple):
    train_no: int
    speed: Union[int, None]
    mileage: Union[Decimal, None]


class LBJ821Time(NamedTuple):
    time: datetime.time


class LBJ866LW:
    pass


class LBJ866Alarm:
    pass


class LBJ866Accident:
    pass


class CIR450LW(NamedTuple):
    locomotive_no: int
    command: bytes
    param: bytes
    more: bytes


class CIR450TDCS:
    def __init__(self, packed_data: bytes):
        data = struct.unpack("<3B4s3s2BH3s3s2H5B3s", packed_data)
        self.dmis_semaphore: int = dmis_semphore_trans.get(data[0], '未知')
        self.semaphore_type: int = dmis_semphore_trans.get(data[1], '未知')
        self.locomotive_type: int = loco_type_trans.get(data[2] & 0x3)
        self.train_no_header: str = data[3].decode('ascii')
        self.train_no_digit: int = int.from_bytes(data[4], 'little')
        self.locomotive_model: int = loco_model_trans.get(data[5], data[5])
        self.locomotive_model_ext: int = data[6]
        self.locomotive_no: int = data[7]
        self.direction, self.mileage, self.is_test = CIR450TDCS._covert_mileage(data[8])
        self.reserved_1, self.train_speed = CIR450TDCS._covert_speed(data[9])
        self.train_weight: int = data[10]
        self.train_length: Decimal = Decimal("%.1f" % (data[11] / 10))
        self.train_carriages: int = data[12]
        self.station_no: int = data[13]
        self.station_no_ext: int = data[14]
        self.segment_no: int = data[15]
        self.segment_no_actual: int = data[16]
        self.driver_id: int = int.from_bytes(data[17], 'little')

    @staticmethod
    def _make(packed_data: bytes):
        return CIR450TDCS(packed_data)

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
            train_mileage = '公里标：%sK%d+%03d' % (sign, int(mileage), mileage % 1 * 1000) + direction

        # Train No 
        train_no = self.train_no_header.strip() + str(self.train_no_digit)
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


class FFSKHeader(NamedTuple):
    mode_word: int
    data_length: int
    address: bytes
    control_word: int
    command_word: int
    function_code: int
    payload_length: int
