import numpy as np 
from matplotlib import pyplot as plt

names = ['group_a','group_b','group_c']
values = [1,10,100]
plt.subplot(131)
plt.bar(names,values)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('Catergorical Plotting')
plt.show()