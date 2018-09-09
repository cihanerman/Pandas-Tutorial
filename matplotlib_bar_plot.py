# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
df = pd.read_csv("iris.csv")

x = np.array([1,2,3,4,5,6,7])
y = x * 2
plt.bar(x,y,label="x vs y")
plt.legend()
plt.title("Bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

