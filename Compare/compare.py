# -*- coding: utf-8 -*-

import csv
import statistics
import matplotlib.pyplot as plt

period = input("周期を入力してください")
cfile = open("./log/sdata_0.csv", "r")#open("./cdata.csv", "r")
sfile = open("./log/sdata_0.csv", "r")#open("./sdata.csv", "r")

ccsv = csv.reader(cfile)
scsv = csv.reader(sfile)
cdata = []
sdata = []
compare = [[], [], []]
for row in ccsv:
    cdata.append(row)
cfile.close()
for row in scsv:
    sdata.append(row)
sfile.close()

lastdata = [cdata[0][0], sdata[0][0]]

for c, s in zip(cdata[1:], sdata[1:]):
    compare[0].append(float(c[0])-float(lastdata[0]))
    compare[1].append(float(s[0])-float(lastdata[1]))
    compare[2].append(abs(float(s[0])-float(c[0])))
    lastdata = [c[0], s[0]]


plt.hist(compare[0], bins=20)
plt.title("Send")
plt.show()

plt.hist(compare[1], bins=20)
plt.title("Rcv.")
plt.show()

plt.hist(compare[2], bins=20)
plt.title("Rcv. - Send")
plt.show()
print("--Send--")
print("mean:{0}".format(statistics.mean(compare[0])))
print("median:{0}".format(statistics.median(compare[0])))

print("--Rcv.--")
print("mean:{0}".format(statistics.mean(compare[1])))
print("median:{0}".format(statistics.median(compare[1])))

print("--(Rcv. - Send)--")
print("mean:{0}".format(statistics.mean(compare[2])))
print("median:{0}".format(statistics.median(compare[2])))
