__author__ = 'Haohan Wang'

import sys

gPath = '/nfs/nas-0-16/hbtrc/genotype/illumina/genotype.txt'
pPath = '/nfs/nas-0-16/hbtrc/phenotype/phenotype.txt'
ePath = "/nfs/nas-0-16/hbtrc/expression/agilent/cerebellum/gene_expression.txt"

def readPhenoType(ppath):
    text = [line.strip() for line in open(ppath)]
    idtext = text[0].split()
    ids = [int(it) for it in idtext[1:]]
    idmap = {} # position 2 id
    idmap2 = {} # id 2 position
    for i in range(len(ids)):
        idmap[i] = ids[i]
        idmap2[ids[i]] = i

    print idmap
    print idmap2

    pheno = {}
    for k in idmap2:
        pheno[k] = []

    phenoList = {}
    for line in text[1:]:
        items = line.split('\t')
        k = int(items[0])
        phenoList[k] = items[1:]

    for k in range(1001, 1044):
        items = phenoList[k]
        print len(items)
        for i in range(len(items)):
            pheno[idmap[i]].append(items[i])
    return pheno

def readExpression(epath):
    text = [line.strip() for line in open(epath)]
    idtext = text[0].split()
    ids = [int(it) for it in idtext[1:]]
    idmap = {} # position 2 id
    idmap2 = {} # id 2 position
    for i in range(len(ids)):
        idmap[i] = ids[i]
        idmap2[ids[i]] = i

    exp = {}
    for k in idmap2:
        exp[k] = []

    c = -1
    t = 0
    for line in text[1:]:
        c+=1
        items = line.split()[1:]
        if c == 0:
            t = len(items)
        if len(items) == t:
            print t, len(items)
            for i in range(len(items)):
                if items[i]!= 'NA':
                    exp[idmap[i]].append(float(items[i]))
                else:
                    exp[idmap[i]].append(0)
    return exp

def saveExpressionPheno(ppath, epath):
    pheno = readPhenoType(ppath)
    ge = readExpression(epath)

    snps = []
    traits = []
    # exp = []
    for k in ge:
        if k in pheno:
            # if k in ge:
                snps.append(ge[k])
                traits.append(pheno[k])
                # exp.append(ge[k])
            # else:
            #     print k, '!'

    f1 = open('ge.csv', 'w')
    c = -1
    for line in snps:
        c += 1
        l = [str(a) for a in line]
        print c, len(l)
        f1.writelines(','.join(l)+'\n')
    f1.close()

    f2 = open('traitsGE.csv', 'w')
    for line in traits:
        f2.writelines(','.join(line)+'\n')
    f2.close()

    # f3 = open('expression.csv', 'w')
    # for line in exp:
    #     f3.writelines(','.join(line)+'\n')
    # f3.close()

if __name__ == '__main__':
    saveExpressionPheno(pPath, ePath)