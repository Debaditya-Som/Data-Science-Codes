
import numpy as np 
from matplotlib import pyplot as plt


plt.figure(1)   #first figure
plt.subplot(211)
plt.plot([1,2,3])
plt.plot (np.array([1,2,3]))
plt.subplot(212)
plt.plot([4,5,6])
plt.plot (np.array([4,5,6]))
# plt.subplot(213)
plt.plot([7,8,9])

plt.figure(2)   #second figure
plt.plot([4,5,6])

plt.figure(3) #third figure
plt.plot([7,8,9])
plt.plot (np.array([7,8,9]))

plt.figure(1)   #first figure current;

plt.figure(2)   #second figure
plt.plot (np.array([4,5,6]))
plt.figure(3)   #first figure current;

plt.subplot(211)    #make subplot(211) in the first figure

plt.title('Easy as 1,2,3') #subplot 211 
