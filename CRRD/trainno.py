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


# 除特殊声明外，数据均来自于《中国铁路列车车次编定表(2018年1月版本)》
# Domestic Train Relegation Definition
point2PointRapidCargoTrainRelegation = (
    (79001, 79040, '哈尔滨局'),
    (79041, 79140, '沈阳局'),
    (79141, 79210, '北京局'),
    (79211, 79250, '太原局'),
    (79251, 79290, '呼和浩特局'),
    (79291, 79340, '郑州局'),
    (79341, 79390, '武汉局'),
    (79391, 79430, '西安局'),
    (79431, 79520, '济南局'),
    (79521, 79610, '上海局'),
    (79611, 79670, '南昌局'),
    (79671, 79740, '广铁集团'),
    (79741, 79780, '南宁局'),
    (79781, 79830, '成都局'),
    (79831, 79870, '昆明局'),
    (79871, 79920, '兰州局'),
    (79921, 79980, '乌鲁木齐局'),
    (79981, 79998, '青藏铁路公司')
)

# X2401-X2999
cargoRapidTrainRelegation = (
    (2401, 2430, '哈尔滨局'),
    (2431, 2480, '沈阳局'),
    (2481, 2510, '北京局'),
    (2511, 2540, '太原局'),
    (2541, 2570, '呼和浩特局'),
    (2571, 2600, '郑州局'),
    (2601, 2630, '武汉局'),
    (2631, 2660, '西安局'),
    (2661, 2690, '济南局'),
    (2691, 2740, '上海局'),
    (2741, 2770, '南昌局'),
    (2771, 2810, '广铁集团'),
    (2811, 2840, '南宁局'),
    (2841, 2890, '成都局'),
    (2891, 2920, '昆明局'),
    (2921, 2950, '兰州局'),
    (2951, 2970, '乌鲁木齐局'),
    (2971, 2990, '青藏铁路公司')
)

# X401-X990
domesticCargoRapidTrainRelegation = (  # Wiki
    (401, 430, '哈尔滨局'),
    (431, 480, '沈阳局'),
    (481, 510, '北京局'),
    (511, 540, '太原局'),
    (541, 570, '呼和浩特局'),
    (571, 600, '郑州局'),
    (601, 630, '武汉局'),
    (631, 660, '西安局'),
    (661, 690, '济南局'),
    (691, 740, '上海局'),
    (741, 770, '南昌局'),
    (771, 810, '广铁集团'),
    (811, 840, '南宁局'),
    (841, 891, '成都局'),
    (891, 920, '昆明局'),
    (921, 950, '兰州局'),
    (951, 970, '乌鲁木齐局'),
    (971, 990, '青藏铁路公司')
)
# 6201-7598
slowNormalPassengerTrainRelegation = (  # Wiki
    (6201, 6300, '哈尔滨局'),
    (6301, 6400, '沈阳局'),
    (6401, 6500, '北京局'),
    (6801, 6850, '太原局'),
    (6851, 6900, '呼和浩特局'),
    (6901, 6950, '郑州局'),
    (6951, 7000, '武汉局'),
    (7001, 7050, '西安局'),
    (7051, 7100, '济南局'),
    (7101, 7200, '上海局'),
    (7201, 7250, '南昌局'),
    (7251, 7300, '广铁集团'),
    (7301, 7350, '南宁局'),
    (7351, 7450, '成都局'),
    (7451, 7500, '昆明局'),
    (7501, 7550, '兰州局'),
    (7551, 7580, '乌鲁木齐局'),
    (7581, 7598, '青藏铁路公司')
)

# 4001-5998
fastNormalPassengerTrainRelegation = (  # Wiki
    (4001, 4200, '哈尔滨局'),
    (4201, 4400, '沈阳局'),
    (4401, 4600, '北京局'),
    (4601, 4650, '太原局'),
    (4651, 4700, '呼和浩特局'),
    (4701, 4800, '郑州局'),
    (4801, 4900, '武汉局'),
    (4901, 5000, '西安局'),
    (5001, 5050, '济南局'),
    (5051, 5200, '上海局'),
    (5201, 5300, '南昌局'),
    (5301, 5500, '广铁集团'),
    (5501, 5550, '南宁局'),
    (5551, 5650, '成都局'),
    (5651, 5700, '昆明局'),
    (5701, 5800, '兰州局'),
    (5801, 5900, '乌鲁木齐局'),
    (5901, 5998, '青藏铁路公司')
)

# K7001-K9850
fastPassengerTrainRelegation = (  # Wiki
    (7001, 7300, '哈尔滨局'),
    (7301, 7600, '沈阳局'),
    (7701, 7800, '北京局'),
    (7801, 7900, '太原局'),
    (7901, 7950, '呼和浩特局'),
    (7951, 8050, '郑州局'),
    (8051, 8150, '武汉局'),
    (8151, 8250, '西安局'),
    (8251, 8350, '济南局'),
    (8351, 8700, '上海局'),
    (8701, 9000, '南昌局'),
    (9001, 9300, '广铁集团'),
    (9301, 9350, '南宁局'),
    (9351, 9600, '成都局'),
    (9601, 9660, '昆明局'),
    (9661, 9740, '兰州局'),
    (9741, 9800, '乌鲁木齐局'),
    (9801, 9850, '青藏铁路公司')
)

# T5001-T9800
expressPassengerTrainRelegation = (  # Wiki
    (5001, 5300, '哈尔滨局'),
    (5301, 5600, '沈阳局'),
    (5601, 6000, '北京局'),
    (6001, 6300, '太原局'),
    (6301, 6400, '呼和浩特局'),
    (6401, 6700, '郑州局'),
    (6701, 7000, '武汉局'),
    (7001, 7300, '西安局'),
    (7301, 7600, '济南局'),
    (7601, 8000, '上海局'),
    (8001, 8300, '南昌局'),
    (8301, 8700, '广铁集团'),
    (8701, 8800, '南宁局'),
    (8801, 9000, '成都局'),
    (9001, 9200, '昆明局'),
    (9201, 9400, '兰州局'),
    (9401, 9600, '乌鲁木齐局'),
    (9601, 9800, '青藏铁路公司')
)

# Y501-Y980
touristTrainRelation = (  # controversial
    (501, 530, '哈尔滨局'),
    (531, 560, '沈阳局'),
    (561, 600, '北京局'),
    (601, 630, '太原局'),
    (631, 640, '呼和浩特局'),
    (641, 670, '郑州局'),
    (671, 700, '武汉局'),
    (701, 730, '西安局'),
    (731, 760, '济南局'),
    (761, 800, '上海局'),
    (801, 830, '南昌局'),
    (831, 870, '广铁集团'),
    (871, 880, '南宁局'),
    (881, 900, '成都局'),
    (901, 920, '昆明局'),
    (921, 940, '兰州局'),
    (941, 960, '乌鲁木齐局'),
    (961, 980, '青藏铁路公司')
)

# Train No Definition
fullTrainNo = (
    (10001, 19998, '技术直达列车', '', None),
    (20001, 29998, '直通货物列车', '', None),
    (30001, 39998, '区段货物列车', '', None),
    (40001, 44998, '摘挂列车', '', None),
    (45001, 49998, '小运转列车', '', None),
    # 单机
    (50001, 50998, '客车单机', '', None),
    (51001, 51998, '货车单机', '', None),
    (52001, 52998, '小运转单机', '', None),
    (53001, 54998, '补机', '', None),
    # (55001, 55998, '试运转列车', '', None),
    (55001, 55300, '试运转普通客、货列车', '', None),
    (55301, 55500, '试运转300km/h以上动车组', 'G', None),
    (55501, 55998, '试运转250km/h动车组', 'D', None),
    (56001, 56998, '轻油动车、轨道车', '', None),
    (57001, 57998, '路用列车', '', None),
    (58101, 58998, '救援列车', '', None),

    (60001, 69998, '自备车列车', '', None),
    (70001, 70998, '超限货物列车', '', None),
    (71001, 72998, '重载货物列车', '', None),  # baidu

    (78001, 78998, '保温列车', '', None),
    (79001, 79998, '“点对点”快速货物列车', '', point2PointRapidCargoTrainRelegation),
    (80001, 81998, '货运五定班列', '', None),
    (82001, 84998, '煤炭直达列车', '', None),
    (85001, 85998, '石油直达列车', '', None),
    (86001, 86998, '始发直达列车', '', None),
    (87001, 87998, '空车直达列车', '', None),
    (88001, 88998, '远程技术直达列车', 'X', None),
    (89001, 89998, '计划外按需列车', '', None),  # 请求来源
    (90001, 91998, '军用列车', '', None),
    (92001, 92998, '伪装军用列车', '', None),  # 请求来源

    (95001, 97998, '抢险救灾列车', '', None),  # 请求来源
    (99001, 99998, '调车作业', '', None)  # 非官方
)

XTrainNo = (
    (1, 199, '特快货物班列(160km/h)', None),
    (201, 398, '快速货物班列(120km/h)', None),
    (401, 998, '管内货物快运列车(120km/h)', domesticCargoRapidTrainRelegation),

    (2401, 2990, '货物快运列车(120km/h)', cargoRapidTrainRelegation),
    (3001, 3098, '时速160km/h特需货物列车', None),
    (3101, 3398, '时速120km/h特需货物列车', None),
    (3401, 3998, '时速80km/h特需货物列车', None),

    (8001, 8998, '中欧、中亚集装箱班列(120km/h)', None),
    (9001, 9500, '中亚集装箱(普通货车标尺)', None),
    (9501, 9998, '水铁联运班列(普通货车标尺)', None)
)

touristTrain = (  # Wiki
    (1, 500, '跨局旅游列车', None),
    (501, 998, '管内旅游列车', touristTrainRelation)
)

temporaryPassengerTrain = (  # Wiki
    (1, 6998, '临时旅客列车', None),
    (7001, 9998, '管内临时旅客列车', None)
)

normalPassengerTrain = (  # Wiki
    (1001, 1998, '跨三局及以上普通旅客快车', None),
    (2001, 2998, '跨两局普通旅客快车', None),
    (4001, 5998, '管内普通旅客快车', fastNormalPassengerTrainRelegation),
    (6001, 6198, '跨局普通旅客慢车', None),
    (6201, 7598, '管内普通旅客慢车', slowNormalPassengerTrainRelegation),
    (7601, 8998, '通勤列车', None)
)

fastPassengerTrain = (  # Wiki
    (1, 4000, '快速列车', None),
    (4001, 4998, '临时快速列车', None),
    (5001, 6998, '管内临时快速列车', None),
    (7001, 9998, '管内快速列车', fastPassengerTrainRelegation)
)

expressPassengerTrain = (  # Wiki
    (1, 3000, '特快列车', None),
    (3001, 3998, '临时特快列车', None),
    (4001, 4998, '管内临时特快列车', None),
    (5001, 9998, '管内特快列车', expressPassengerTrainRelegation)
)

directExpressPassengerTrain = (  # Wiki
    (1, 4000, '直达特快列车', None),
    (4001, 4998, '临时直达特快列车', None),
    (5001, 9000, '管内直达特快列车', None),
    (9001, 9998, '管内临时直达特快列车', None)
)

EMUTrain = (  # Wiki
    (1, 4000, '动车组列车', None),
    (4001, 4998, '临时动车组列车', None),
    (5001, 9000, '管内动车组列车', None),
    (9001, 9998, '管内临时动车组列车', None)
)

intercityEMUTrain = (  # Wiki
    (1, 9000, '城际动车组列车', None),
    (9001, 9998, '临时城际动车组列车', None)
)

highSpeedEMUTrain = (  # Wiki
    (1, 4000, '高速动车组列车', None),
    (4001, 4998, '临时高速动车组列车', None),
    (5001, 9000, '管内高速动车组列车', None),
    (9001, 9998, '管内临时高速动车组列车', None)
)

DJTrainNo = (  # Wiki
    (1, 400, '直通300km/h检测列车', None),
    (401, 998, '管内300km/h检测列车', None),
    (1001, 1400, '直通250km/h检测列车', None),
    (1401, 1998, '管内250km/h检测列车', None),

    (5001, 6998, '直通动车组确认列车', None),
    (7001, 8998, '管内动车组确认列车', None)
)

returningTrain = (
    (1, 100, '有火回送动车组车底', None),
    (101, 298, '无火回送动车组车底', None),
    (301, 498, '回送普通客车底', None)
)


def searchTrainNoDigit(trainNoDigit, queryTable, queryCapital=False):
    desc = '未知列车'
    capital = ''
    relegation = None
    relegationTable = None
    for entry in queryTable:
        if entry[0] <= int(trainNoDigit) <= entry[1]:
            if queryCapital:
                desc, capital, relegationTable = entry[2:]
            else:
                desc, relegationTable = entry[2:]
            break
    if relegationTable is not None:
        for entry in relegationTable:
            if entry[0] <= int(trainNoDigit) <= entry[1]:
                relegation = entry[2]
                break
    if queryCapital:
        return desc, capital, relegation
    else:
        return desc, relegation


def resolveTrainNo(trainNo):
    # 车次 描述 归属
    capital, desc, relegation = '', None, None
    trainNo = str(trainNo)
    idx = 0
    for idx, c in enumerate(trainNo):
        if trainNo[idx:].isdigit():
            break
    capital = trainNo[:idx]
    trainNo = trainNo[idx:]
    # Validate train no
    if not trainNo or not trainNo.isdigit() or int(trainNo) <= 0:
        raise ValueError("Invalid train no: {}".format(capital + trainNo))
    if len(trainNo) > 2 and trainNo[0] == '0':
        if not capital == '':
            raise ValueError("Invalid train no: {}".format(capital + trainNo))
        if trainNo[1] == '0':
            capital = '00'
            trainNo = trainNo[2:]
        else:
            capital = '0'
            trainNo = trainNo[1:]
    # Search train no
    if capital == '00':
        desc, relegation = searchTrainNoDigit(trainNo, returningTrain)
    elif capital in ['0', '0K', '0T', '0Z'] and len(trainNo) <= 4:
        desc = '回送图定客车底'
    elif capital.startswith('F'):
        desc = '因故折返列车'
    elif capital == '' and len(trainNo) == 5:
        desc, capital, relegation = searchTrainNoDigit(trainNo, fullTrainNo, queryCapital=True)
    elif capital == 'X':
        if len(trainNo) == 5:
            desc, _, relegation = searchTrainNoDigit(trainNo, fullTrainNo, queryCapital=True)
            desc += '(挂有快运车辆)'
        else:
            desc, relegation = searchTrainNoDigit(trainNo, XTrainNo)
    elif capital == 'G':
        desc, relegation = searchTrainNoDigit(trainNo, highSpeedEMUTrain)
    elif capital == 'C':
        desc, relegation = searchTrainNoDigit(trainNo, intercityEMUTrain)
    elif capital == 'D':
        desc, relegation = searchTrainNoDigit(trainNo, EMUTrain)
    elif capital == 'DJ':
        desc, relegation = searchTrainNoDigit(trainNo, DJTrainNo)
    elif capital == 'KJ':
        desc = '客检车'
    elif capital == 'S':
        desc = '市郊旅客列车'
    elif capital == 'Z':
        desc, relegation = searchTrainNoDigit(trainNo, directExpressPassengerTrain)
    elif capital == 'T':
        desc, relegation = searchTrainNoDigit(trainNo, expressPassengerTrain)
    elif capital == 'K':
        desc, relegation = searchTrainNoDigit(trainNo, fastPassengerTrain)
    elif capital == '' and len(trainNo) == 4:
        desc, relegation = searchTrainNoDigit(trainNo, normalPassengerTrain)
    elif capital == 'L':
        desc, relegation = searchTrainNoDigit(trainNo, temporaryPassengerTrain)
    elif capital == 'Y':
        desc, relegation = searchTrainNoDigit(trainNo, touristTrain)
    else:
        desc = '未知列车'

    return capital, trainNo, desc, relegation
