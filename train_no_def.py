def Point2PointRapidCargoTrain(trainNo):
    return None


def CargonRapidTrain(trainNo):
    return None


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
    (79001, 79998, '“点对点”快速货物列车', '', Point2PointRapidCargoTrain),
    (80001, 81998, '货运五定班列', '', None),
    (82001, 84998, '煤炭直达列车', '', None),
    (85001, 85998, '石油直达列车', '', None),
    (86001, 86998, '始发直达列车', '', None),
    (87001, 87998, '空车直达列车', '', None),
    (88001, 88998, '远程技术直达列车', 'X', None),
    (89001, 89998, '计划外按需列车', '', None),  # not list on file
    (90001, 91998, '军用列车', '', None),
    (92001, 92998, '伪装军用列车', '', None),  # 请求来源

    (95001, 97998, '抢险救灾列车', '', None),  # not list on file
    (99001, 99998, '调车作业', '', None)  # not offical
)

XtrainNo = {
    (1, 199, '特快货物班列(160km/h)', None),
    (201, 398, '快速货物班列(120km/h)', None),
    (401, 998, '货物快运列车(120km/h)', None),

    (2401, 2990, '货物快运列车(120km/h)', CargonRapidTrain),
    (3001, 3098, '时速160km/h特需货物列车', None),
    (3101, 3398, '时速120km/h特需货物列车', None),
    (3401, 3998, '时速80km/h特需货物列车', None),

    (8001, 8998, '中欧、中亚集装箱班列(120km/h)', None),
    (9001, 9500, '中亚集装箱(普通货车标尺)', None),
    (9501, 9998, '水铁联运班列(普通货车标尺)', None),
}

normalPassengerTrain = {  # Wiki
    (1001, 1998, '跨三局及以上普通旅客快车', None),
    (2001, 2998, '跨两局普通旅客快车', None),
    (4001, 5998, '管内普通旅客快车', None),
    (6001, 6198, '跨局普通旅客慢车', None),
    (6201, 7598, '管内普通旅客慢车', None),
    (7601, 8998, '通勤列车', None),
}

DJTrainNO = {
    (1, 400, '直通300km/h检测列车', None),
    (401, 998, '管内300km/h检测列车', None),
    (1001, 1400, '直通250km/h检测列车', None),
    (1401, 1998, '管内250km/h检测列车', None),

    (5001, 6998, '直通动车组确认列车', None),
    (7001, 8998, '管内动车组确认列车', None)
}


def resolveTrainNo(trainNo):
    # 车次 描述 归属
    trainNo = str(trainNo)
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
    elif capital in ['0K', '0T', '0Z'] and len(trainNo) <= 4:
        desc = '回送图定客车底'
    elif capital == 'F':
        desc = '因故折返列车'
    elif capital in ['X', ''] and len(trainNo) == 5:
        found = False
        for entry in fullTrainNo:
            if entry[0] <= int(trainNo) <= entry[1]:
                desc, capital, relegation = entry[2:]
                found = True
        if not found:
            desc = '未知列车'
    elif capital == 'X':
        found = False
        for entry in XtrainNo:
            if entry[0] <= int(trainNo) <= entry[1]:
                desc, relegation = entry[2:]
                found = True
        if not found:
            desc = '未知列车'
    elif capital == 'G':
        desc = '高速动车组列车'
    elif capital == 'C':
        desc = '城际列车'
    elif capital == 'D':
        desc = '动车组列车'
    elif capital == 'DJ':
        found = False
        for entry in DJTrainNO:
            if entry[0] <= int(trainNo) <= entry[1]:
                desc, relegation = entry[2:]
                found = True
        if not found:
            desc = '未知列车'
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
        found = False
        for entry in normalPassengerTrain:
            if entry[0] <= int(trainNo) <= entry[1]:
                desc, relegation = entry[2:]
                found = True
        if not found:
            desc = '普通旅客列车'
    elif capital == 'L':
        desc = '临时旅客列车'
    elif capital == 'Y':
        desc = '旅游列车'
    else:
        desc = '未知列车'

    return capital, trainNo, desc, relegation


if __name__ == '__main__':
    print(resolveTrainNo('0K184'))
