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
            if i>0 and i % 2500 == 0:
                l.append(items[i])
        m = ','.join(l)
        f1.writelines(m+'\n')
    f1.close()

    f2 = open(path+'marker_subsampled description.csv', 'w')
    for i in range(len(d)):
        if i> 0 and i % 2500 == 0:
            f2.writelines(d[i]+'\n')
    f2.close()

def sampleAccordingToChromo(ch):
    marker = [line.strip() for line in open(path+'markers.csv')]
    d = [line.strip() for line in open('../data/marker.txt')][1:]
    f2 = open(path+'marker_subsampled description.csv', 'w')
    ind = []
    c = 0
    for i in range(len(d)):
        items = d[i].split()
        if items[3] == str(ch):
            c+=1
            if c % 100 == 0:
                ind.append(i)
                f2.writelines(items[1]+'\n')
    f2.close()

    f1 = open(path+'marker_subsampled.csv', 'w')
    for line in marker:
        items = line.split(',')
        m = ','.join(items[i] for i in ind)
        f1.writelines(m+'\n')
    f1.close()

def sampleCriticalGenes():
    import numpy as np
    marker = [line.strip() for line in open(path+'markers.csv')]
    d = [line.strip() for line in open('../data/marker.txt')][1:]
    f2 = open(path+'marker_subsampled description.csv', 'w')
    ind = []
    c = 0

    text = [line.strip() for line in open('../data/gwas_alzheimer.tsv')]
    snpD = {}
    for line in text[1:]:
        items = line.split('\t')
        try:
            pvalue = float(items[27])
        except:
            pvalue = 1
        snp = items[21]
        if snp not in snpD:
            snpD[snp] = pvalue
        else:
            if pvalue < snpD[snp]:
                snpD[snp] = pvalue

    for i in range(len(d)):
        items = d[i].split()
        name = items[1]
        if name in snpD:
            ind.append(i)
            f2.writelines(items[1]+'\n')
        else:
            p = np.random.random()
            if p < 5e-4:
                ind.append(i)
                f2.writelines(items[1]+'\n')
    f2.close()

    f1 = open(path+'marker_subsampled.csv', 'w')
    for line in marker:
        items = line.split(',')
        m = ','.join(items[i] for i in ind)
        f1.writelines(m+'\n')
    f1.close()


if __name__ == '__main__':
    sampleCriticalGenes()