# -*- coding: utf-8 -*-
import pandas as pd

dic = {"name":["cihan","fatma","erkan","aydın","mert","kubi"],
        "age":[26,48,23,50,25,24],
        "maas":[100,200,300,400,500,600]}

dataFrame1 = pd.DataFrame(dic) #Data frame oluşturma
print dataFrame1 
head = dataFrame1.head() # Bastan 5 satırı getirir içene istediğimiz değeri yazınca okadarınıda getiriyor Örn:head(100)
print head
tail = dataFrame1.tail() # Sondan 5 satırı getirir içene istediğimiz değeri yazınca okadarınıda getiriyor Örn:tail(100)
print tail
print dataFrame1.columns # Sütun isimlerini yazdırır
print dataFrame1.info() # Frame hakında bilgi verir
print dataFrame1.dtypes # Framedeki sütünların tiplerini verir
print dataFrame1.describe() # Sayısal değerler hakında basit çıktılar verir.
