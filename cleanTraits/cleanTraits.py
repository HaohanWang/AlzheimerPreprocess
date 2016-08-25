__author__ = 'Haohan Wang'

text = [line.strip() for line in open('../data/traits.csv')]

data = []
for line in text:
    l = []
    items = line.split(',')
    for i in range(len(items)):
        if i < 26:
            if items[i] == 'NA':
                l.append('0')
            else:
                l.append(items[i])
        elif i == 27:
            if items[i] == 'NA':
                l.append('no')
            else:
                l.append(items[i])
        elif i == 28:
            if items[i] == 'NA':
                l.append('M')
            else:
                l.append(items[i])
        elif i == 31 or i == 32:
            if items[i] == 'affected':
                l.append('1')
            else:
                l.append('0')
        else:
            l.append(items[i])

    data.append(l)

f = open('../data/traits_clean.csv', 'w')
for line in data:
    f.writelines(','.join(line)+'\n')
f.close()