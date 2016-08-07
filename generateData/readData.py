__author__ = 'Haohan Wang'

#/nfs/nas-0-16/hbtrc/genotype/

import sys

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
        base = items[0]
        for i in range(len(items)):
            if items[i] == base:
                v = 0
            else:
                v = 1
            geno[idmap[i]].append(v)
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
        items = line.split()
        k = int(items[0])
        phenoList[k] = items[1:]

    for k in range(1001, 1044):
        items = phenoList[k]
        for i in range(len(items)):
            pheno[idmap[i]].append(items[i])
    return pheno

def saveGenoPheno(gpath, ppath):
    geno = readGenotype(gpath)
    pheno = readPhenoType(ppath)

    snps = []
    traits = []
    for k in geno:
        if k in pheno:
            snps.append(geno[k])
            traits.append(pheno[k])

    f1 = open('snps.csv', 'w')
    for line in snps:
        l = [str(a) for a in line]
        f1.writelines(','.join(l)+'\n')
    f1.close()

    f2 = open('traits.csv', 'w')
    for line in traits:
        f2.writelines(','.join(line)+'\n')
    f2.close()

if __name__ == '__main__':
    saveGenoPheno(gPath, pPath)
