import numpy as np 
from matplotlib import pyplot as plt


plt.figure(1)   #first figure
plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])

plt.figure(2)   #second figure
plt.plot([4,5,6])

plt.figure(1)   #first figure current;

plt.subplot(211)    #make subplot(211) in the first figure

plt.title('Easy as 1,2,3') #subplot 211 

plt.show()