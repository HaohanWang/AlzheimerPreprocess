__author__ = 'Haohan Wang'

import numpy as np

snps = np.loadtxt('../cleanedData/all/marker value.csv', delimiter=',')
np.save('../cleanedData/all/snps', snps)

phenos = np.loadtxt('../cleanedData/all/traits value.csv', delimiter=',')
np.save('../cleanedData/all/phenos', phenos)