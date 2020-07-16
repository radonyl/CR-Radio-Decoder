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

loco_model_trans = {
    1: "JF",
    3: "QJ",
    5: "JS",
    6: "KD7",
    # 工程机械
    55: "LJKC",
    57: "JW2",
    58: "GQ164",
    59: "JY29010",
    60: "JZW3",
    61: "JW5",
    62: "JY29010P",
    63: "HS280",
    64: "240",
    65: "HS260",
    66: "GCS220",
    68: "JY290",
    69: "JY2905",
    70: "JY360",
    71: "JY230",

    81: "DF21",
    # 内燃机车
    101: 'DF',
    102: 'DF2',
    103: 'DF3',
    104: 'DF4B',
    105: 'DF4R',  # 客运型
    106: 'DF4C',
    107: 'DF5',
    108: 'DF5R',  # 口岸型
    109: 'DF6',
    110: 'DF7',
    111: 'DF8',
    112: 'DF9',
    113: 'DF10',
    114: 'DFH1',
    115: 'DFH2',
    116: 'DFH3',
    117: 'DFH5',
    118: 'BJ',
    119: 'BJR',
    120: 'ND2',
    121: 'ND3',
    122: 'ND4',
    123: 'ND5',
    124: "NY5",
    125: "NY6",
    126: "NY7",
    127: "QY",
    128: "DFH21",
    129: "DF7B",
    130: "DF5R0",  # 口岸型
    131: "DF7C",
    132: "DF7S",
    133: "GK1",
    134: "GK1F",
    135: "DF4E",
    136: "DF7D",
    137: "GK1A",
    138: "DF11",
    139: "TA",
    140: "DF10F",
    141: "DF4D",
    142: "DF8B",
    143: "DF12",
    144: "DF7E",
    145: "NYJ1",
    146: "NYJ2",
    147: "NZJ2",
    148: "DF4DJ",
    149: "NDJ1",
    150: "NDJ2",
    151: 'NJ2',
    152: 'DF7G',
    156: 'DF11Z',
    158: 'DF11G',

    # “和谐”内燃机车
    160: 'HXN3',
    161: 'HXN5',
    162: 'HXN3B',
    163: 'HXN5B',

    191: "DF4DH",

    201: "8G",
    202: "8K",
    203: "6G",
    204: "6K",
    # “韶山”电力机车
    205: "SS1",
    206: 'SS3',
    207: 'SS4',
    208: 'SS5',
    209: 'SS6',
    210: 'SS3G',
    211: 'SS7',
    212: 'SS8',
    213: 'SS7B',
    214: 'SS7C',
    215: 'SS6B',
    216: 'SS9',
    217: 'SS7D',
    # 早期国产电力动车组
    218: "DJ",
    219: "DJ1",
    220: "DJ2",
    221: "DJF",
    222: "DJJ1",
    223: "DJF",

    224: 'SS7E',
    225: "SSJ3",
    226: "SS3C",
    229: "HX",
    230: "KTT",
    # “和谐”电力机车
    231: 'HXD1',
    232: 'HXD2',
    233: 'HXD3',
    234: 'HXD1B',
    235: 'HXD2B',
    236: 'HXD3B',
    237: 'HXD1C',
    238: 'HXD2C',
    239: 'HXD3C',
    240: 'HXD1D',
    241: 'HXD2D',
    242: 'HXD3D',
    243: "HXD1F",
    244: "HXD2F",

    254: "CQDC",
    # 高原内燃机车
    300: '雪域神舟',
    # 动车组列车
    301: 'CRH1A',
    302: 'CRH2A',
    303: 'CRH3',
    304: 'CRH380AL',
    305: 'CRH5A',
    306: 'CRH3C',
    307: 'CRH380BG',
    308: 'CRH380A',
    309: 'CRH380D',
    310: 'CRH380B',
    311: 'CRH380BL',

    313: 'CRH2B',
    314: 'CRH2C',
    315: 'CRH2E',
    316: "CRH6F",

    319: 'CRH1B',

    # 工程机械
    330: "CJ-1",
    331: "CJ-2",
    351: "JW3",
    352: "JW4",
    353: "JW7",
    354: "TY2",
    355: "TY5",
    356: "TY6",
    357: "DB7B",
    358: "DA8",
    359: "DA11",
    360: "DA12",
    361: "DA220",
    381: "JZW4",
    382: "DAX",
    391: "QGC16",
    392: "QGC25",
    801: "NS1600",
}

dmis_semphore_trans = {
    0: '始发车',
    1: '编组站',
    2: '出站',
    3: '进站',
    4: '通过',
    5: '预告',
    6: '容许',
    7: '预留',
    8: '预留'
}

loco_type_trans = {
    0b00: '货车本务',
    0b10: '货车补机',
    0b01: '客车本务',
    0b11: '客车补机'
}

lw_cmd = {
    # References:
    # 1. TB/T 2973-2006 列车尾部安全防护装置及附属设备 p.8-p.9
    # 2. 列车防护报警和客车列尾系统技术条件V1.0 [铁道部运输局 2009.11]
    # LOCO->LW
    0x24: '排风',
    0x25: '排风应答',
    0x91: '查询风压',
    0x92: '查询风压应答',
    0x83: '消号',
    0x84: '消号应答',  # ref.1 only
    0xb5: '输号',
    0xb6: '输号应答',
    # LW->LOCO
    0x30: '列尾主机风压报警',
    0x31: '风压报警应答',
    0xb0: '列尾主机电池欠压报警',
    0xb1: '欠压报警应答',
    0x5b: '列尾主机输号请求',
    # KLW
    0x93: '自动查询风压命令',  # ref.2 only
    0x94: '自动查询风压应答',  # ref.2 only
    0xa1: '时钟校准信息',  # ref.2 only
    0xa2: '时钟校准应答',  # ref.2 only
    0xa3: '风压校准信息',  # ref.2 only
    0xa4: '风压校准应答',  # ref.2 only
}

lbj_func = {
    # References:
    # 1. TJ/DW 012—2009
    # 2. TB/T 3504-2018
    0x01: "列车防护报警信息",
    0x02: "列车防护报警解除信息",
    0x03: "道口事故报警信息",  # updated in ref.2
    0x04: "道口事故报警解除信息",  # updated in ref.2
    0x05: "施工防护报警信息",  # updated in ref.2
    0x06: "施工防护报警解除信息",  # updated in ref.2
    0x07: "出入库检测命令",
    0x08: "报警试验信息",
}

lbj_alarm_cleared_reason_trans = {
    0x01: '报警解除',
    0x04: '30s收不到报警消息'
}

lbj_alarm_source_trans = {
    0x01: '控制盒1或MMI1',
    0x02: '控制盒2或MMI2',
    0x03: '主机面板'
}

lbj_test_port_trans = {
    0x03: '控制盒1或MMI1',
    0x04: '控制盒2或MMI2'
}

dispatch_cmd_func = {
    0x01: '调度命令',
    0x02: '路票',
    0x03: '绿色许可证',
    0x04: '红色许可证',
    0x05: '出站跟踪调车通知书',
    0x06: '轻型车辆使用书',
    0x07: '列车接车进路预告信息',
    0x08: '正线通过',
    0x09: '侧线通过',
    0x0a: '正线缓行通过',
    0x0b: '进站正线停车',
    0x0c: '进站侧线停车',

    0x11: '调车作业',
    0x12: '调车请求已收到',

    **dict.fromkeys(list(range(0x18, 0x1f + 1)), '其他信息'),
    0x20: '出入库检测'
}

dispatch_reply_name_trans = {
    0x80: '请求入库检',  # 表示对入库检设备发送入库检请求命令
    0x81: '已自动确认',  # 表示对调度命令的自动确认信息
    0x82: '已签收',  # 表示对调度命令的签收信息

    0x91: '请求调车',  # 表示对向TDCS发送调车请求命令
}
