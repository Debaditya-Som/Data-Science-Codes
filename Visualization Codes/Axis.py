#Code to plot axis of a graph 
import numpy as np
from matplotlib import pyplot as plt


plt.plot(np.array([1,2,3,4]),'ro')
plt.axis([0,6,0,20,0,30,0,40])
plt.show()
