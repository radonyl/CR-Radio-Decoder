## Introduction to CRRD
CRRD: China railway radio decoder. It supports the following packages:
- POCSAG type
    - LBJ Train notice
    - LBJ Time sync
- FFSK type
    - TDCS wireless train no
    - TDCS wireless dispatching command (**partly untested**)
    - CIR cargo train tail device (partly supported)
    - LBJ passage train tail device (**partly untested**)
    - LBJ train protection alarm (**totally untested**)
- Train no resolve
    - use CRRD.resolveTrainNo
## Installation
CRRD support Python3.8+ only(may also 3.7, but untested). It can be install using pip:
```shell script
pip install CRRD
```
or simply copy CRRD module directory to your project

## Usage
```python
import CRRD
import binascii
# FFSK Example
line = "CIRFSK(45):0c 2b 00 3f 1f 00 00 1f 8c 30 20 03 03 01 20 20 20 54 70 00 00 f2 00 09 02 33 b7 11 7c 44 02 c8 03 95 01 11 82 00 f1 01 6e c3 41 ce b1 "
data = binascii.a2b_hex(line.split(':')[-1].replace(' ', ''))
package = CRRD.FFSKDecoder.decode(data) # CIR450TrainNo(train_no=T112, speed=124, mileage=1161.011)
package.to_string() # '客车本务 HXD3D-0521 担当T112次 特快列车 公里标：K1161+011(-) 速度：124km/h 总重: 968t 辆数:17 计长:40.5 区段号:241 1 司机号:4309870 车站号:130 进站'

# POCSAG Example
s = '11101 123 11882'
CRRD.POCSAGDecoder.decode(s, address=1234000) # LBJ821Notice(train_no=11101, speed=123, mileage=Decimal('1188.2'))
s = '1]231  23 11323'
CRRD.POCSAGDecoder.decode(s, address=1234000) # CRRD.decoder.BrokenPackage: Broken Package: Part1

# Resolve train no
CRRD.resolveTrainNo('6162') # ('', '6162', '跨局普通旅客慢车', None)
CRRD.resolveTrainNo('7465') # ('', '7465', '管内普通旅客慢车', '昆明局')
CRRD.resolveTrainNo('X101') # ('X', '101', '特快货物班列(160km/h)', None)
CRRD.resolveTrainNo('88392J') # ValueError: Invalid train no: 88392J
```


## Bug Report
feel free to report bug or request a feature on Github issue