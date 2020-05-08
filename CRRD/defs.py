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


locoTypeTable = {
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

dmisSemphoreTrans = {
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

locoTypeStateTable = {
    0b00: '货车本务',
    0b10: '货车补机',
    0b01: '客车本务',
    0b11: '客车补机'
}

lwCmd = {
    0x24: '排风命令',
    0x25: '排风应答',
    0x91: '查询风压命令',
    0x92: '查询风压应答',
    0x83: '消号命令',
    0x84: '消号应答',
    0xb5: '输号命令',
    0xb6: '输号应答',
    0x30: '列尾主机风压报警',
    0x31: '风压报警应答',
    0xb0: '列尾主机电池欠压报警',
    0xb1: '欠压报警应答',
    0x5b: '列尾主机输号请求'
}
