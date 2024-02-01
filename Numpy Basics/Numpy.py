import numpy as np
#np works as an alias for numpy

myarr = np.array([[3,4,5,6]] , np.int8) 
#here datatype in the np.array is integer
print(myarr)
myarr[0,1]
myarr.shape

#matrix multiplication

#method 1
res1 = a@b
print("res1\n",res1)
print()

#method 2
res2 = a.dot(b)
print("res2\n", res2)
print()

#method 3
res3 = np.dot(a,b)
print("res3\n", res3)
print()
