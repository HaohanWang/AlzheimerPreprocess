__author__ = 'Haohan Wang'

import numpy as np

def calculateSNPsFeature():
    snps = np.loadtxt('../cleanedData/AMPL/markers_values.csv', delimiter=',')
    shp = snps.shape
    n = np.random.random([shp[1], 2])
    n[n<0.5] = 0
    n[n>0.5] = 1
    m = np.mean(snps, 0)
    print m.shape
    n[:,1] = m
    np.savetxt('../cleanedData/AMPL/markers_features.csv', n, delimiter=',')

def calculateCorrelation():
    y = np.loadtxt('../cleanedData/GF/traits_values.csv', delimiter=',')
    m = np.corrcoef(y.T)
    np.savetxt('../cleanedData/GF/graph.csv', m, delimiter=',')


if __name__ == '__main__':
    calculateCorrelation()
