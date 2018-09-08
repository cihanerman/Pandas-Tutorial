# -*- coding: utf-8 -*-
import pandas as pd

dic = {"name":["cihan","fatma","erkan","aydın","mert","kubi"],
        "age":[26,48,23,50,25,24],
        "maas":[100,200,300,400,500,600]}

dataFrame1 = pd.DataFrame(dic) #Data frame oluşturma

print dataFrame1["name"] # Sütüna erişim
print dataFrame1.age # Sütüna erişim
dataFrame1["worktime"] = [2,5,6,7,8,4] # Yeni sütün ekleme
print dataFrame1.loc[:,"age"] # age sütünu ve tüm satırlar
print dataFrame1.loc[:3,"age"] # age sütunu ve 3 indexli satıra kadar
print dataFrame1.loc[:3,["age","name"]] # age sütunundan name sütünuna 3 indexli satıra kadar
print dataFrame1.loc[::-1] # Frame'i tersten sıralar
print dataFrame1.loc[:,"name"] # Name sütunu ve tüm satırlar
print dataFrame1.iloc[:,2] # Tüm satırlar ve 2 indexli sütun(name)