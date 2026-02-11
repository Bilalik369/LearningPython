import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

x = 2 * np.random.random((100, 1))   
y = 4 + 3 * x + np.random.randn(100, 1)


plt.scatter(x, y, color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Synthetic Data")
plt.show()



