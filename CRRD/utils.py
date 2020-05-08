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


def hex2int(l, reverse=False):
    if isinstance(l, str):
        return int(l, 16)
    l = l[::-1] if reverse else l
    return int(''.join(l), 16)


def hex2bcd(l):
    return ''.join(l).translate(
        {ord('a'): '?', ord('b'): 'B', ord('c'): ' ', ord('d'): '-', ord('e'): ']', ord('f'): '['})


def hex2ascii(l):
    return binascii.a2b_hex(''.join(l)).decode('ascii')


def crc16(data):
    return binascii.crc_hqx(binascii.a2b_hex(''.join(data)), 0)
