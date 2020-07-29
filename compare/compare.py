# -*- coding: utf-8 -*-

import csv
import statistics
import matplotlib.pyplot as plt

period = input("周期を入力してください")
cfile, sfile = [], []
ccsv, scsv = [], []
for i in range(3):
    try:
        cfile.append(open("../log/sdata{0}.csv".format(i), "r"))
        sfile.append(open("../log/sdata{0}.csv".format(i), "r"))
    except FileNotFoundError:
        continue

for c, s in zip(cfile, sfile):
    ccsv.append(csv.reader(c))
    scsv.append(csv.reader(s))
cdata = [[] for _ in range(len(ccsv))]
sdata = [[] for _ in range(len(scsv))]
compares = [[[], [], []] for _ in range(len(cfile))]
lags = []
for i in range(len(ccsv)):
    for row in ccsv[i]:
        cdata[i].append(row)

for i in range(len(scsv)):
    for row in scsv[i]:
        sdata[i].append(row)

for c, s in zip(cfile, sfile):
    c.close()
    s.close()


print(len(cdata))
for i in range(len(cdata)):
    lastdata = [cdata[i][0][0], sdata[i][0][0]]
    print(lastdata)
    for c, s in zip(cdata[i][1:], sdata[i][1:]):
        compares[i][0].append(float(c[0])-float(lastdata[0]))
        compares[i][1].append(float(s[0])-float(lastdata[1]))
        compares[i][2].append(abs(float(s[0])-float(c[0])))
        lastdata = [c[0], s[0]]
for compare in compares:
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

for i in range(len(cdata[0])):
    lags.append(float(cdata[0][i][0])-float(cdata[1][i][0]))
plt.hist(lags, bins=20)
plt.title("Rcv.1 - Rcv.2")
plt.show()
