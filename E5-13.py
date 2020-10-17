# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********pandas 内部结合的基本********#
data1 = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
         "year": [2001, 2002, 2001, 2008, 2006],
         "amount": [1, 4, 5, 6, 3]}
data2 = {"fruits": ["apple", "orange", "banana", "strawberry", "mango"],
         "year": [2001, 2002, 2001, 2008, 2007],
         "price": [150, 120, 100, 250, 3000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
# 以df1和df2中的"fruits"列为Key，通过内部结合的方式合并成新的DataFrame变量df3;
df3 = pd.merge(df1, df2, on="fruits", how="inner")
print(df3)
