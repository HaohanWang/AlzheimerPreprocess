__author__ = 'Haohan Wang'

import numpy as np

from matplotlib import pyplot as plt

graph = np.loadtxt('../cleanedData/GF/graph.csv', delimiter=',')
plt.imshow(graph)
plt.show()