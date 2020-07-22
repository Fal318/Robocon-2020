import csv
import time
import bluetooth as bt
import struct
import RN42
import address as ad
addr = ad.client_address

res_data = []

ras = RN42.RN42("ras", ad.client_address, 1)
ras.connectBluetooth(ras.bdAddr, ras.port)

for i in range(256*40):
    try:
        data = i % 256
        ras.sock.send((data).to_bytes(1, "little"))
        res_data.append([time.time(), data])
    except KeyboardInterrupt:
        ras.disConnect(ras.sock)
file = open("./sdata.csv", "w")

w = csv.writer(file)
w.writerows(res_data)
file.close()