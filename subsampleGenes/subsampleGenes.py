__author__ = 'Haohan Wang'

path = "/home/haohanwang/Downloads/AlzData/"

def subSample():
    marker = [line.strip() for line in open(path+'markers.csv')]
    d = [line.strip() for line in open(path+'marker description.csv')]

    f1 = open(path+'marker_subsampled.csv', 'w')
    for line in marker:
        items = line.split(',')
        l = []
        for i in range(len(items)):
            if i>0 and i % 100 == 0:
                l.append(items[i])
        m = ','.join(l)
        f1.writelines(m+'\n')
    f1.close()

    f2 = open(path+'marker_subsampled description.csv', 'w')
    for i in range(len(d)):
        if i> 0 and i % 100 == 0:
            f2.writelines(d[i]+'\n')
    f2.close()

if __name__ == '__main__':
    subSample()