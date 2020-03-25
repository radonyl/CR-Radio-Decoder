def hex2int(l, reverse=False):
    if isinstance(l, str):
        return int(l, 16)
    l = l[::-1] if reverse else l
    return int(''.join(l), 16)


bcdCharTable = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?', 'B', ' ', '-', ']', '[')  # 800Mhz LBJ


def hex2bcd(l):
    return ''.join(map(lambda x: bcdCharTable[x], [int(i, 16) for i in ''.join(l)]))


def hex2ascii(l):
    if isinstance(l, str):
        return chr(int(l, 16))
    return ''.join([chr(int(i, 16)) for i in l])


def hexStr(l):
    return '0x' + ''.join(l).lower()


locoTypeTable = {
    # 内燃机车
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

    128: 'DFH21',
    129: 'DF7B',
    130: 'DF5R0',  # 口岸型
    131: 'DF7C',

    141: 'DF4D',
    142: 'DF8B',
    143: 'DF12',

    151: 'NJ2',
    152: 'DF7G',
    156: 'DF11Z',
    158: 'DF11G',
    # “和谐”内燃机车
    160: 'HXN3',
    161: 'HXN5',
    162: 'HXN3B',
    163: 'HXN5B',
    # “韶山”电力机车
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

    224: 'SS7E',
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

    319: 'CRH1B'
}
tdcsSemphoreTrans = {
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
