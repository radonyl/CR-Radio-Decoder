from cir_utils import *
from decimal import Decimal
from train_no_def import resolveTrainNo


class UnkownPackage(ValueError):
    pass


class NotPackage(ValueError):
    pass


class BrokenPackage(ValueError):
    pass


class ParseError(ValueError):
    pass


class CIR450Package(object):
    """
    reference: TB/T 3052-2002
    """
    def __init__(self, packageData):
        self.modeWord = hexStr(packageData[0])
        self.dataLength = hex2int(packageData[1])
        self.addr = hexStr(packageData[2:7])
        self.controlWord = hexStr(packageData[7])
        self.commandWord = hexStr(packageData[8])
        self.functionCode = hexStr(packageData[9])
        self.payloadLength = hex2int(packageData[10])
        self.payload = packageData[11:-2]
        self.crc = hexStr(packageData[-2:])
        if len(self.payload) != self.payloadLength:
            raise BrokenPackage('Payload incomplete!')

    def decode(self):
        if self.addr == '0x003f1f0000' and \
                self.controlWord == '0x1f' and \
                self.commandWord == '0x8c' and \
                self.functionCode == '0x30':
            return CIR450TrainNoPackage(self.payload)
        elif (self.addr == '0x413f1f0000' or
              self.addr == '0x413f1f0001') and \
                self.controlWord == '0x1f' and \
                self.commandWord == '0x8c' and \
                self.functionCode == '0xa5':
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
    """
    def __init__(self, payload):
        self.type = 'tdcs'
        try:
            self.parse(payload)
        except Exception as e:
            raise ParseError(e)

    def __repr__(self):
        fullTrainNo = self.trainNoHeader.strip() + str(self.trainNoDigit)
        return 'CIR TrainNoPkg' + fullTrainNo

    def parse(self, payload):
        # self.payload = payload
        self.tdcsSemaphore = hex2int(payload[0])  # 10
        self.semaphoreType = hex2int(payload[1])  # 11
        self.locoType = hex2int(payload[2])  # 12
        self.trainNoHeader = hex2ascii(payload[3:7])  # 13
        self.trainNoDigit = hex2int(payload[7:10], reverse=True)  # 14
        trainNo = self.trainNoHeader.strip() + str(self.trainNoDigit)
        _, _, desc, _ = resolveTrainNo(trainNo)
        self.trainNoDesc = desc

        self.locoModel = hex2int(payload[10])
        self.locoModelExt = hex2int(payload[11])
        self.locoNo = hex2int(payload[12:14], reverse=True)

        trainMileage = hex2int(payload[14:17], reverse=True) & 0x3fffff
        self.trainMileage = Decimal("%.3f" % (trainMileage / 1000))
        self.trainSpeed = hex2int(payload[17:20], reverse=True) & 0x3ff
        self.trainWeight = hex2int(payload[20:22], reverse=True)
        trainLength = hex2int(payload[22:24], reverse=True)
        self.trainLength = Decimal("%.1f" % (trainLength / 10))
        self.trainCarriages = hex2int(payload[24])

        self.stationNo = hex2int(payload[25])
        self.stationNoExt = hex2int(payload[26])

        self.segmentNo = hex2int(payload[27])
        self.segmentActualNo = hex2int(payload[28])

        self.driverId = hex2int(payload[29:32], reverse=True)  # Different to Standard
        # self.driverIdExt   = hex2int(payload[31])

    def show(self):
        tdcsState = tdcsSemphoreTrans.get(self.tdcsSemaphore & 0x0f, '未定义')
        locoType = locoTypeStateTable.get(self.locoType & 0x03)
        locomotive = locoTypeTable.get(self.locoModel, str(self.locoModel)) + '-' + "%04d" % self.locoNo
        trainNo = self.trainNoHeader.strip() + str(self.trainNoDigit) + '次'
        trainDesc = self.trainNoDesc
        trainInfo = "总重: %dt 辆数:%d 计长:%.1f" % (self.trainWeight, self.trainCarriages, self.trainLength)
        trainMileage = "公里标：K%d+%03d" % (int(self.trainMileage), self.trainMileage % 1 * 1000)
        trainSpeed = "速度：%dkm/h" % self.trainSpeed
        segment = '区段号: ' + str(self.segmentNo) + ' ' + str(self.segmentActualNo)
        driver = '司机号:' + str(self.driverId)
        station = '车站号:' + str(self.stationNo)
        info = ' '.join((locoType, locomotive, '担当' + trainNo, trainDesc,
                         trainMileage, trainSpeed, trainInfo, segment, driver, station, tdcsState))
        print(info)
        return info


if __name__ == "__main__":
    import os
    asb_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(asb_dir, 'cir_test', 'cir_test.log'), 'r') as f:
        cir_logs = f.read()
    for line in filter(lambda x: bool(x.strip()), cir_logs.split('\n')):
        print(line)
        pkg = CIR450Package(line.strip()[21:].split(' ')).decode()
        pkg.show()
