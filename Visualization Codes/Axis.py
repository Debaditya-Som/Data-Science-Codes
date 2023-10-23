#Code to plot axis of a graph 

from matplotlib import pyplot as plt
import numpy as np

plt.plot(np.array([1,2,3,4],[1,4,9,16]),'ro')
plt.axis([0,6,0,20])
plt.show()
