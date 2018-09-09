# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv("iris.csv")

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.hist(setosa.PetalLengthCm,label="setosa")
plt.legend()
plt.xlabel("PetalLengthCm Values")
plt.ylabel("Frekans")
plt.title("Histogram Plot")
plt.grid()
plt.show()

