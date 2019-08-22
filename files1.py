import numpy as np 

a = ([[2,4], [3,5]])
print(a)

np.savetxt("test1.cvs",a , delimiter=",")

a = np.genfromtxt("test1.cvs", delimiter=",")
print(a)