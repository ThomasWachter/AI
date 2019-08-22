import matplotlib.pyplot as plt 
import numpy as np

y = [1,2,3,4]

# los valores de x

plt.plot([i**2 for i in y], y)

plt.show()