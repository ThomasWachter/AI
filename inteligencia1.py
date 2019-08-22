import numpy  as np 
import pandas as pd


arr = np.array([1,2,3,4,5,6,7,8,9])

series = pd.Series(arr)

# print(series)

dict1 = {"a":1, "b": 2, "c": 3}

series1 = pd.Series(dict1)

# print(series1)
# print(series1[2:4])

list1 = [1,2,3,4,5,6]
list2 = [{"a": 1, "b": 2}, {"a":23, "b": 21}, {"a": 73, "b": 32}]

table2 = pd.DataFrame(list2, index = ["fila1", "fila2", "fila3"])


# print(table)
print(table2)