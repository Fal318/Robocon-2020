import csv
import statistics
import matplotlib.pyplot as plt
cfile = open("./cdata.csv", "r")
sfile = open("./sdata.csv", "r")

ccsv = csv.reader(cfile)
scsv = csv.reader(sfile)
cdata = []
sdata = []
compare = [[], []]
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
    lastdata = [c[0], s[0]]

#fig, ax = plt.subplots()
plt.hist(compare[0])
#ax.vlines(statistics.median(compare[0]), 0, 10000, "red")
plt.show()
plt.hist(compare[0])
#ax.vlines(statistics.median(compare[0]), 0, 10000, "red")
plt.show()
print(statistics.median(compare[0]))
print(statistics.mean(compare[1]))
print(False in compare[1])
