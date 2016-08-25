__author__ = 'Haohan Wang'

gPath = '/nfs/nas-0-16/hbtrc/genotype/illumina/genotype.txt'
pPath = '/nfs/nas-0-16/hbtrc/phenotype/phenotype.txt'

def readGenotype(gpath):
    text = [line.strip() for line in open(gpath)]
    idtext = text[0].split()
    ids = [int(it) for it in idtext[1:]]
    idmap = {} # position 2 id
    idmap2 = {} # id 2 position
    for i in range(len(ids)):
        idmap[i] = ids[i]
        idmap2[ids[i]] = i

    geno = {}
    for k in idmap2:
        geno[k] = []

    for line in text[1:]:
        items = line.split()[1:]
        for i in range(len(items)):
            m = items[i].split('/')
            geno[idmap[i]].extend(m)
    return geno

def readPhenoType(ppath):
    text = [line.strip() for line in open(ppath)]
    idtext = text[0].split()
    ids = [int(it) for it in idtext[1:]]
    idmap = {} # position 2 id
    idmap2 = {} # id 2 position
    for i in range(len(ids)):
        idmap[i] = ids[i]
        idmap2[ids[i]] = i

    pheno = {}
    for k in idmap2:
        pheno[k] = []

    phenoList = {}
    for line in text[1:]:
        items = line.split('\t')
        k = int(items[0])
        phenoList[k] = items[1:]

    k = 1029
    items = phenoList[k]
    print len(items)
    for i in range(len(items)):
        if items[i] == 'F':
            v = '2'
        elif items[i] == 'M':
            v = '1'
        else:
            v = 'N'
        pheno[idmap[i]].append(v)
    return pheno

def saveGenoPheno(gpath, ppath):
    pheno = readPhenoType(ppath)
    geno = readGenotype(gpath)

    snps = []
    for k in geno:
        if k in pheno:
            m = ['FAM0', str(k), '0', '0', pheno[k], '0']
        else:
            m = ['FAM0', str(k), '0', '0', 'N', '0']
        m.extend(geno[k])
        snps.append(m)

    f1 = open('snps.ped', 'w')
    for line in snps:
        # l = [str(a) for a in line]
        f1.writelines('\t'.join(line)+'\n')
    f1.close()


if __name__ == '__main__':
    saveGenoPheno(gPath, pPath)