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
    (79981, 79998, '青藏公司')
)

cargonRapidTrainRelegation = (
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
    (2971, 2990, '青藏公司')
)

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
    (55001, 55300, '普通客、货列车', '', None),
    (55301, 55500, '300km/h以上动车组', 'G', None),
    (55501, 55998, '250km/h动车组', 'D', None),
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
    (401, 998, '货物快运列车(120km/h)', None),

    (2401, 2990, '货物快运列车(120km/h)', cargonRapidTrainRelegation),
    (3001, 3098, '时速160km/h特需货物列车', None),
    (3101, 3398, '时速120km/h特需货物列车', None),
    (3401, 3998, '时速80km/h特需货物列车', None),

    (8001, 8998, '中欧、中亚集装箱班列(120km/h)', None),
    (9001, 9500, '中亚集装箱(普通货车标尺)', None),
    (9501, 9998, '水铁联运班列(普通货车标尺)', None),
)

normalPassengerTrain = (  # Wiki
    (1001, 1998, '跨三局及以上普通旅客快车', None),
    (2001, 2998, '跨两局普通旅客快车', None),
    (4001, 5998, '管内普通旅客快车', None),
    (6001, 6198, '跨局普通旅客慢车', None),
    (6201, 7598, '管内普通旅客慢车', None),
    (7601, 8998, '通勤列车', None),
)

DJTrainNO = (
    (1, 400, '直通300km/h检测列车', None),
    (401, 998, '管内300km/h检测列车', None),
    (1001, 1400, '直通250km/h检测列车', None),
    (1401, 1998, '管内250km/h检测列车', None),

    (5001, 6998, '直通动车组确认列车', None),
    (7001, 8998, '管内动车组确认列车', None)
)


def searchTrainNoDigit(trainNoDigit, queryTable, queryCaptital=False):
    desc = '未知列车'
    capital = ''
    relegation = None
    relegationTable = None
    for entry in queryTable:
        if entry[0] <= int(trainNoDigit) <= entry[1]:
            if queryCaptital:
                desc, capital, relegationTable = entry[2:]
            else:
                desc, relegationTable = entry[2:]
            break
    if relegationTable is not None:
        for entry in relegationTable:
            if entry[0] <= int(trainNoDigit) <= entry[1]:
                relegation = entry[2]
                break
    if queryCaptital:
        return desc, capital, relegation
    else:
        return desc, relegation


def resolveTrainNo(trainNo):
    trainNo = str(trainNo)
    # 车次 描述 归属
    capital, desc, relegation = '', None, None
    while not trainNo.isdigit():
        capital += trainNo[0]
        trainNo = trainNo[1:]
    if trainNo.startswith('00') and capital == '':
        no = int(trainNo[2:])
        if 1 <= no <= 100:
            desc = '有火回送动车组车底'
        elif 101 <= no <= 298:
            desc = '无火回送动车组车底'
        elif 301 <= no <= 498:
            desc = '回送普通客车底'
        else:
            desc = '未知列车'
    elif (trainNo.startswith('0') or capital in ['0K', '0T', '0Z']) and len(trainNo) <= 4:
        desc = '回送图定客车底'
    elif capital.startswith('F'):
        desc = '因故折返列车'
    elif capital in ['X', ''] and len(trainNo) == 5:
        desc, capital, relegation = searchTrainNoDigit(trainNo, fullTrainNo, queryCaptital=True)
    elif capital == 'X':
        desc, relegation = searchTrainNoDigit(trainNo, XTrainNo)
    elif capital == 'G':
        desc = '高速动车组列车'
    elif capital == 'C':
        desc = '城际列车'
    elif capital == 'D':
        desc = '动车组列车'
    elif capital == 'DJ':
        desc, relegation = searchTrainNoDigit(trainNo, DJTrainNO)
    elif capital == 'KJ':
        desc = '客检车'
    elif capital == 'S':
        desc = '市郊旅客列车'
    elif capital == 'Z':
        desc = '直达特快列车'
    elif capital == 'T':
        desc = '特快列车'
    elif capital == 'K':
        desc = '快速列车'
    elif capital == '' and len(trainNo) == 4:
        desc, relegation = searchTrainNoDigit(trainNo, normalPassengerTrain)
    elif capital == 'L':
        desc = '临时旅客列车'
    elif capital == 'Y':
        desc = '旅游列车'
    else:
        desc = '未知列车'

    return capital, trainNo, desc, relegation


if __name__ == '__main__':
    print(resolveTrainNo('57001'))
    print(resolveTrainNo('X2433'))
    print(resolveTrainNo('0184'))
    print(resolveTrainNo('FK342'))
    print(resolveTrainNo('DJ1342'))
