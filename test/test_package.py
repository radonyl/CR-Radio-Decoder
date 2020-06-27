import binascii
import os
import sqlite3
import datetime
from CRRD.decoder import FFSKDecoder, POCSAGDecoder, BrokenPackage, UnknownPackage, EmptyPackage

abspath = os.path.dirname(__name__)


# Test POCSAG
def test_POCSAG():
    db = sqlite3.connect(os.path.join(abspath, 'messages.db'))
    cursor = db.cursor()
    cursor.execute("SELECT * from messages")
    for i in cursor.fetchall():
        msg_id, msg_addr, msg_data, msg_source, msg_time, _ = i
        msg_time = datetime.datetime.fromtimestamp(msg_time)
        try:
            if msg_addr in ['1234000', '1234008']:
                pkg = POCSAGDecoder.decode(msg_data, int(msg_addr))
                if msg_addr == '1234008':
                    recv_time = msg_time.time()
                    if not (recv_time.hour == pkg.time.hour and recv_time.minute == pkg.time.minute):
                        pass
                        # print('Clock deviation:', recv_time, pkg.time)
                if msg_addr == '1234000':
                    pass
                    #print(pkg)
            elif msg_addr in ['003f1f0000']:
                data = binascii.a2b_hex(msg_data.split(':')[-1].replace(' ', ''))
                pkg = FFSKDecoder.decode(data)
                print(msg_time, pkg.to_string())
        except BrokenPackage:
            pass
            # print(f'Broken {[msg_addr, msg_data]}')
        except UnknownPackage:
            pass
            # print(f'Unknown {[msg_addr, msg_data]}')
        except EmptyPackage:
            pass
            # print(f'Empty {[msg_addr, msg_data]}')


# Test FFSK
def test_FFSK():
    with open(os.path.join(abspath, "cir_raw_200507.log"), 'r') as f:
        for line in f:
            line = line.strip()
            idx = line.find('CIRFSK')
            if idx == -1:
                continue
            timestamp = line[:idx]
            data = binascii.a2b_hex(line[idx:].split(':')[-1].replace(' ', ''))
            FFSKDecoder.decode(data)


test_POCSAG()
