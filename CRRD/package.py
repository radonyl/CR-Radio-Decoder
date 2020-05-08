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


from CRRD.utils import *
from CRRD.defs import *
from CRRD.trainno import resolveTrainNo
from decimal import Decimal


class UnkownPackage(ValueError):
    pass


class NotPackage(ValueError):
    pass


class BrokenPackage(ValueError):
    pass


class ParseError(ValueError):
    pass


class LBJ821Package(object):
    # TODO: LBJ state machine support
    def __init__(self, packageData):
        pass
        self.trainNoDigit = 0
        self.trainMileage = 0
        self.speed = 0
        self.source = None


class CIR450Package(object):
    """
    reference: TB/T 3052-2002
    """

    def __init__(self, packageData, ignoreCrc=True):
        self.modeWord = hex2int(packageData[0])
        self.dataLength = hex2int(packageData[1])
        self.addr = hex2int(packageData[2:7])
        self.controlWord = hex2int(packageData[7])
        self.commandWord = hex2int(packageData[8])
        self.functionCode = hex2int(packageData[9])
        self.payloadLength = hex2int(packageData[10])
        self.payload = packageData[11:-2]
        self.crc = hex2int(packageData[-2:])

        if len(self.payload) != self.payloadLength:
            raise BrokenPackage('Payload incomplete!')
        self.crcValid = crc16(packageData[:-2]) == self.crc
        if not ignoreCrc and not self.crcValid:
            raise BrokenPackage('Corrupted Data!')

    def decode(self):
        if self.addr == 0x003f1f0000 and \
                self.controlWord == 0x1f and \
                self.commandWord == 0x8c and \
                self.functionCode == 0x30:
            return CIR450TrainNoPackage(self.payload)
        elif (self.addr == 0x413f1f0000 or
              self.addr == 0x413f1f0001) and \
                self.controlWord == 0x1f and \
                self.commandWord == 0x8c and \
                self.functionCode == 0xa5:
            return CIR450LWPackage(self.payload)

        else:
            raise UnkownPackage(self.__str__())

    def __str__(self):
        return 'CIR: addr:%s ctrl:%s cmd:%s func:%s' % \
               (self.addr, self.controlWord, self.commandWord, self.functionCode)


class CIR450LWPackage(object):
    """
    reference: TB/T 2973-2006
    """

    def __init__(self, payload):
        self.type = 'lw'
        try:
            self.parse(payload)
        except Exception as e:
            raise ParseError(e)

    def __repr__(self):
        return 'CIR LW loco:%s cmd:%s param:%s' % (self.locoNo, self.command, self.param)

    def parse(self, payload):
        self.payload = payload
        self.locoNo = hex2bcd(payload[0:2])
        self.command = hex2int(payload[2:4]) & 0x00ff  # high byte reserved
        self.param = hex2bcd(payload[4:6])
        # without more specified field found in TB/T 2973-2006

    def show(self):
        loco = str(self.locoNo) + '机车'
        _str = loco + lwCmd.get(self.command, '未知命令') + self.param
        print(_str)
        return _str


class CIR450TrainNoPackage(object):
    """
    reference: GSM-R数字移动通信应用技术条件 第二分册：列车无线车次号校核信息传送系统
               TJ/DW014-2012 GSM-R数字移动通信应用技术条件 第九分册：数据传输应用接口及设备
    """

    def __init__(self, payload):
        self.type = 'dmis'
        try:
            self.parse(payload)
        except Exception as e:
            raise ParseError(e)

    def __repr__(self):
        fullTrainNo = self.trainNoHeader.strip() + str(self.trainNoDigit)
        return 'CIR TrainNoPkg' + fullTrainNo

    def parse(self, payload):
        # self.payload = payload
        self.dmisSemaphore = hex2int(payload[0])  # 10
        self.semaphoreType = hex2int(payload[1])  # 11 identical to # 10
        self.locoType = hex2int(payload[2])  # 12
        # parse train no info
        self.trainNoHeader = hex2ascii(payload[3:7])  # 13
        self.trainNoDigit = hex2int(payload[7:10], reverse=True)  # 14
        self.trainNo = self.trainNoHeader.strip() + str(self.trainNoDigit)
        try:
            _, _, trainNoDesc, trainRelegation = resolveTrainNo(self.trainNo)
        except ValueError:
            trainNoDesc = '无效车次'
            trainRelegation = None
        if trainRelegation is None:
            trainRelegation = ''
        self.trainNoDesc = trainNoDesc
        self.trainRelegation = trainRelegation
        # parse locomotive info
        self.locoModel = hex2int(payload[10])
        self.locoModelExt = hex2int(payload[11])
        self.locoNo = hex2int(payload[12:14], reverse=True)
        # parse train mileage
        trainMileage = hex2int(payload[14:17], reverse=True)
        isTestData = False
        direction = None
        if trainMileage in [9999888, 8888888]:  # test data patterns
            isTestData = True
        elif trainMileage == 0xffffff or trainMileage == 9999999:
            # mileage == 0xfffff means no mileage data available
            # mileage == 9999999 means this package is only for the station CTC and will not be forwarded further.
            trainMileage = 9999999
        else:
            flag = trainMileage >> 22
            trainMileage &= 0x3fffff
            if flag >> 1:
                trainMileage = -trainMileage
            direction = flag & 0x01
        self.trainMileage = Decimal("%.3f" % (trainMileage / 1000))
        self.isTestData = isTestData
        self.direction = direction
        # parse train properties
        self.trainSpeed = hex2int(payload[17:20], reverse=True) & 0x3ff
        # print((hex2int(payload[17:20], reverse=True) & 0xffffc00) >> 10)  # TODO: What's this ?
        self.trainWeight = hex2int(payload[20:22], reverse=True)
        trainLength = hex2int(payload[22:24], reverse=True)
        self.trainLength = Decimal("%.1f" % (trainLength / 10))
        self.trainCarriages = hex2int(payload[24])
        # parse train monitor info
        self.stationNo = hex2int(payload[25])
        self.stationNoExt = hex2int(payload[26])

        self.segmentNo = hex2int(payload[27])
        self.segmentActualNo = hex2int(payload[28])

        self.driverId = hex2int(payload[29:32], reverse=True)  # Different to Standard
        # self.driverIdExt   = hex2int(payload[31])

    def show(self):
        dmisState = dmisSemphoreTrans.get(self.dmisSemaphore & 0x0f, '未定义')
        locoType = locoTypeStateTable.get(self.locoType & 0x03)
        locomotive = locoTypeTable.get(self.locoModel, str(self.locoModel)) + '-' + "%04d" % self.locoNo
        trainInfo = '总重: %dt 辆数:%d 计长:%.1f' % (self.trainWeight, self.trainCarriages, self.trainLength)

        if self.direction is None:
            direction = '(x)'
        else:
            direction = '(+)' if self.direction else '(-)'

        if self.trainMileage < 0:
            sign = '-'
            mileage = abs(self.trainMileage)
        else:
            sign = ''
            mileage = self.trainMileage

        trainMileage = '公里标：%sK%d+%03d' % (sign, int(mileage), mileage % 1 * 1000) + direction
        trainSpeed = '速度：%dkm/h' % self.trainSpeed
        segment = '区段号:' + str(self.segmentNo) + ' ' + str(self.segmentActualNo)
        driver = '司机号:' + str(self.driverId)
        station = '车站号:' + str(self.stationNo)
        info = ' '.join((locoType, locomotive, '担当%s次 %s%s' % (self.trainNo, self.trainRelegation, self.trainNoDesc),
                         trainMileage, trainSpeed, trainInfo, segment, driver, station, dmisState))
        if self.isTestData:
            info += '(测试数据)'
        print(info)
        return info
