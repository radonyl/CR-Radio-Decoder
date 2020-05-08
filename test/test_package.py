import os
from CRRD.package import CIR450Package, BrokenPackage, ParseError

abspath = os.path.dirname(__name__)
with open(os.path.join(abspath, "cir_test.log"), 'r') as f:
    for line in f:
        line = line.strip()
        idx = line.find('CIRFSK')
        if idx == -1:
            continue
        timestamp = line[:idx]
        data = line[idx:].split(':')[-1].split(' ')
        try:
            CIR450Package(packageData=data, ignoreCrc=False).decode().show()
        except BrokenPackage:
            print("CRC failure: ")
            CIR450Package(packageData=data).decode().show()
            input("Press any key to continue...")
