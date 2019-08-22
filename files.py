import numpy as np  

arr = np.array([[1,2],[2,5]])

print(arr)

np.savetxt("test.txt",arr)
# aqui guardamos el arreglo como archivo txt

newarr = np.loadtxt("test.txt")
print(newarr)