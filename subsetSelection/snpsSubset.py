__author__ = 'Haohan Wang'

text = [line.strip() for line in open('../data/snps.csv')]

data = []

for line in text:
    items = line.split(',')
    l = []
    for i in range(0, 555000, 555):
        l.append(items[i])
    data.append(l)

markers = [line.strip() for line in open('../data/marker.csv')]

m = [markers[i] for i in range(0, 555000, 555)]

f1 = open('../data/markers_values.csv', 'w')
for line in data:
    f1.writelines(','.join(line)+'\n')
f1.close()

f2 = open('../data/markers_labels.csv', 'w')
for line in m:
    f2.writelines(line+'\n')
f2.close()
