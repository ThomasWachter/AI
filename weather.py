# vamos a estudiar la regresion lineal
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


data = pd.read_csv("Weather.csv")
# print(data)
# print(data.shape)
# print(data.describe()) #de aqui sabemos que tenempos 21 variables que definen el clima 

data.plot(x="MaxTemp", y="MinTemp",style="o")
plt.title("maxima temperatura vs minima temperatura")
plt.xlabel("temperaturaminima")
plt.ylabel("temperaturamaxima")
# plt.show()

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(data["MaxTemp"])
plt.plot()

# https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f
# https://www.youtube.com/watch?v=JMUxmLyrhSk&t=4291s