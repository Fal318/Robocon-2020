import csv
import time
import bluetooth as bt
import struct
import RN42
import address as ad
addr = ad.client_address


class Main:
    ras = RN42.RN42("ras", ad.client_address, 1)
    ras.connectBluetooth(ras.bdAddr,ras.port)

    for i in range(10000):
        try:
            ras.sock.send((i//256).to_bytes(1, "little"))
        except KeyboardInterrupt:
            ras.disConnect(ras.sock)