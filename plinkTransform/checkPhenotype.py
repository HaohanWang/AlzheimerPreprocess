__author__ = 'Haohan Wang'

def checkMapFile(gpath):
    text = [line.strip() for line in open(gpath)][1:]
    marker = []
    count = 0
    for line in text:
        items = line.split()
        marker.append((items[3], items[1], '0', items[-1]))
        if items[3] == '0':
            print line, count
        count += 1
    # f1 = open('snps.map', 'w')
    # for a in marker:
    #     f1.writelines('\t'.join(a) + '\n')
    # f1.close()

if __name__ == '__main__':
    checkMapFile('/nfs/nas-0-16/hbtrc/genotype/illumina/marker.txt')