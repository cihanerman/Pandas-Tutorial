# -*- coding: utf-8 -*-
import pandas as pd

dic = {"name":["cihan","fatma","erkan","aydın","mert","kubi"],
        "age":[26,48,23,50,25,24],
        "maas":[100,200,300,400,500,600]}

dataFrame1 = pd.DataFrame(dic) #Data frame oluşturma
ortalama_maas = dataFrame1.maas.mean()
print ortalama_maas
dataFrame1["maas_seviyesi"] = ["yüksek" if ortalama_maas < each else "düşük" for each in dataFrame1.maas]
dataFrame1.columns = [each.upper() for each in dataFrame1.columns]
print dataFrame1
