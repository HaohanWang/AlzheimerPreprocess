__author__ = 'Haohan Wang'

gPath = '/nfs/nas-0-16/hbtrc/genotype/illumina/marker.txt'
pPath1 = '/nfs/nas-0-16/hbtrc/phenotype/phenotype_description.txt'
pPath2 = '/nfs/nas-0-16/hbtrc/phenotype/phenotype.txt'

def getMarkerName(gpath):
    text = [line.strip() for line in open(gpath)][1:]
    marker = []
    for line in text:
        marker.append(line.split()[1])
    f1 = open('marker.csv', 'w')
    for a in marker:
        f1.writelines(a + '\n')
    f1.close()

def getTraitName(ppath1, ppath2):
    text = [line.strip() for line in open(ppath1)][1:]
    i2d = {}
    for line in text:
        items = line.split()
        i2d[items[0]] = items[1]
    text = [line.strip() for line in open(ppath2)][1:]
    traits = []
    for line in text:
        i = line.split()[0]
        traits.append(i2d[i])
    f2 = open('traits_d.csv', 'w')
    for l in traits:
        f2.writelines(l+'\n')
    f2.close()

if __name__ == '__main__':
    getMarkerName(gPath)
    getTraitName(pPath1, pPath2)