__author__ = 'Haohan Wang'

#/nfs/nas-0-16/hbtrc/genotype/

import sys

gPath = '/nfs/nas-0-16/hbtrc/genotype/illumina/genotype.txt'
pPath = '/nfs/nas-0-16/hbtrc/phenotype/phenotype.txt'
ePath = "/nfs/nas-0-16/hbtrc/expression/agilent/cerebellum/gene_expression.txt"

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

def saveGenoPheno(gpath, ppath, epath):
    pheno = readPhenoType(ppath)
    geno = readGenotype(gpath)
    # ge = readExpression(epath)

    snps = []
    traits = []
    # exp = []
    for k in geno:
        if k in pheno:
            # if k in ge:
                snps.append(geno[k])
                traits.append(pheno[k])
                # exp.append(ge[k])
            # else:
            #     print k, '!'

    f1 = open('snps.csv', 'w')
    for line in snps:
        l = [str(a) for a in line]
        f1.writelines(','.join(l)+'\n')
    f1.close()

    f2 = open('traits.csv', 'w')
    for line in traits:
        f2.writelines(','.join(line)+'\n')
    f2.close()

    # f3 = open('expression.csv', 'w')
    # for line in exp:
    #     f3.writelines(','.join(line)+'\n')
    # f3.close()

def saveExpression(epath):
    # text = [line.strip() for line in open(epath)]
    # idtext = text[0].split()
    # ids = [int(it) for it in idtext[1:]]
    # idmap = {} # position 2 id
    # idmap2 = {} # id 2 position
    # for i in range(len(ids)):
    #     idmap[i] = ids[i]
    #     idmap2[ids[i]] = i
    #
    # ge = {}
    # for k in idmap2:
    #     ge[k] = []
    #
    # geList = {}
    # geneIDs = []
    # for line in text[1:]:
    #     items = line.split('\t')
    #     k = int(items[0])
    #     geneIDs.append(k)
    #     geList[k] = items[1:]
    #
    # for k in geneIDs:
    #     items = geList[k]
    #     print len(items)
    #     for i in range(len(items)):
    #         ge[idmap[i]].append(items[i])
    # return ge
    text = [line.strip() for line in open(epath)][1:]
    f3 = open('expression.csv', 'w')
    f4 = open('geneID.csv', 'w')
    idl = []
    for line in text:
        items = line.split('\t')
        id = items[0]
        idl.append(id)
        m = []
        for tmp in items[1:]:
            if tmp == 'NA':
                m.append('0')
            else:
                m.append(tmp)
        f3.writelines(','.join(m)+'\n')
        f4.writelines(id+'\n')
    f3.close()
    f4.close()


if __name__ == '__main__':
    saveGenoPheno(gPath, pPath, ePath)
    # saveExpression(ePath)