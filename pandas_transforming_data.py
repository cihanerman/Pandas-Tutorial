# -*- coding: utf-8 -*-
import pandas as pd

dic = {"name":["cihan","fatma","erkan","aydın","mert","kubi"],
        "age":[26,48,23,50,25,24],
        "maas":[100,200,300,400,500,600]}

dataFrame1 = pd.DataFrame(dic) #Data frame oluşturma
dataFrame1["list_comp"] = [each * 2 for each in dataFrame1.age] # yeni sütun oluturma 1 ve data manüplasyonu
print dataFrame1

def multiply(age):
    return age * 2

dataFrame1["apply_metod"] = dataFrame1.age.apply(multiply) # yeni sütun oluturma 2 ve data manüplasyonu
print dataFrame1
