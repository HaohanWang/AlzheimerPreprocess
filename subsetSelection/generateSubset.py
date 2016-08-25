__author__ = 'Haohan Wang'

def selectSNPSubset(text, mini, maxi):
    return text[mini:maxi]

def selectTraitSubset(trait, mini, maxi):
    return trait[mini:maxi]

def selectTraits(trait, indices):
    tr = []
    for l in trait:
        items = l.split(',')
        n = [items[i] for i in indices]
        tr.append(n)
    return tr

def writeMarkers(filepath, markers):
    f = open(filepath, 'w')
    for line in markers:
        f.writelines(line + '\n')
    f.close()

def writeTraits(filepath, traits):
    f = open(filepath, 'w')
    for line in traits:
        f.writelines(','.join(line)+'\n')
    f.close()


if __name__ == '__main__':
    markers_text = [line.strip() for line in open('../data/markers_values.csv')]
    traits_text = [line.strip() for line in open('../data/traits_clean.csv')]
    markers = selectSNPSubset(markers_text, 100, 200)
    traits = selectTraitSubset(traits_text, 100, 200)
    groups = selectTraits(traits, [28])
    traits = selectTraits(traits, [7,8,9,10])
    markers = selectTraits(markers, xrange(200))
    grp = []
    for line in groups:
        if line[0] == 'F':
            grp.append(['0'])
        else:
            grp.append(['1'])

    writeTraits('../cleanedData/TL/markers_values.csv', markers)
    writeTraits('../cleanedData/TL/traits_values.csv', traits)
    # writeTraits('../cleanedData/MPL/groups_id.csv', grp)

