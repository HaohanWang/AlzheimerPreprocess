__author__ = 'Haohan Wang'

path = "/home/haohanwang/Downloads/AlzData/"

def subsamplePheno():
    index = [i for i in range(3, 8)] + [32]
    pheno = [line.strip() for line in open(path + 'traits_clean.csv')]
    f1 = open(path+'traits_sub.csv', 'w')
    for line in pheno:
        items = line.split(',')
        newItem = [items[i-1] for i in index]
        l = ','.join(newItem)
        f1.writelines(l+'\n')
    f1.close()

    des = [line.strip() for line in open('../traints/phenotype_description.csv')][1:]
    f2 = open(path+'traits_sub description.csv', 'w')
    for i in range(len(des)):
        line = des[i]
        item = line.split()[1]
        if i+1 in index:
            f2.writelines(item+'\n')
    f2.close()


if __name__ == '__main__':
    subsamplePheno()
