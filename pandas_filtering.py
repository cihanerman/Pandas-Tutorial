# -*- coding: utf-8 -*-
import pandas as pd

dic = {"name":["cihan","fatma","erkan","aydın","mert","kubi"],
        "age":[26,48,23,50,25,24],
        "maas":[100,200,300,400,500,600]}

dataFrame1 = pd.DataFrame(dic) #Data frame oluşturma
filter1 = dataFrame1.maas > 200 # Maası 200 den büyük olanlar
print filter1
filter_date = dataFrame1[filter1] # Filter kullanma yöntemi 1
print filter_date
filter2 = dataFrame1.age < 26
print filter2
print dataFrame1[filter1 & filter2] # iki filter'ı birlikte kullanma
print dataFrame1[dataFrame1.age > 26] # Filter kullanma yöntemi 2
