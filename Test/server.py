import csv
import sys
import time
import signal
import asyncio
import traceback
import bluetooth as bt
import struct
import RN42
import address as ad
addr = ad.client_address

res_data = []


def connect():
    try:
        global ras
        ras = RN42.RN42("ras", ad.client_address, 1)
        ras.connectBluetooth(ras.bdAddr, ras.port)
    except:
        sys.exit("Connection Failed")
    else:
        print("connect")


def main(signum, frame):
    data = 1
    ras.sock.send((data).to_bytes(1, "little"))
    res_data.append([time.time(), data])
    print("send:{0}".format(data))



def write_logs():
    file = open("./sdata.csv", "w")
    w = csv.writer(file)
    w.writerows(res_data)
    file.close()


if __name__ == "__main__":
    connect()
    try:
        signal.signal(signal.SIGALRM, main)
        signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    except:
        traceback.print_exc()
    write_logs()
