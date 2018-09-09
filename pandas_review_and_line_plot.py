# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv("iris.csv")
#print  df
print df.Species.unique() # Sütundki benzersiz değerleri yazdırır.
print df.info()
print df.describe()
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]
print setosa.describe()
print versicolor.describe()

df1 = df.drop(["Id"],axis=1)
print df1
# df1.plot() # diyagram çizer
# plt.show() # çizlen diyagramı gösterir
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa",alpha=0.5)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor",alpha=0.5)
plt.plot(virginica.Id,virginica.PetalLengthCm,color="brown",label="virginica",alpha=0.5)
plt.xlabel("Id") # x eksenine isim verir
plt.ylabel("PetalLengthCm") # y eksenine isim verir
plt.grid(color='gray', linestyle='-', linewidth=1) # diyagrama grid çizgileri ekler
plt.legend() # Diyagramda ismleri bir karade gösterir. İçine değer yazılmazsa en uygun yerde gösterir.
plt.show()