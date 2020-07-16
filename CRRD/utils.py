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


import binascii


def hex2int(s, reverse=False):
    if isinstance(s, str):
        return int(s, 16)
    s = s[::-1] if reverse else s
    return int(''.join(s), 16)


def hex2bcd(s):
    if isinstance(s, bytes):
        return hex2bcd(bytes2hex(s))
    elif isinstance(s, str):
        return s.translate(
            {ord('a'): '?', ord('b'): 'B', ord('c'): ' ', ord('d'): '-', ord('e'): ']', ord('f'): '['})
    else:
        raise ValueError


def bytes2hex(s):
    if isinstance(s, bytes):
        return binascii.b2a_hex(s).decode('ascii')
    else:
        raise ValueError


def decimal2mileage(d):
    return "K%d+%03d" % (int(d), d % 1 * 1000)


def hex2ascii(s):
    return binascii.a2b_hex(''.join(s)).decode('ascii')


def crc16(data):
    return binascii.crc_hqx(data, 0)
