# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********pandas设置索引和列标签2********#
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
series1 = pd.Series(data1, index=index)  # 通过index参数指定索引
series2 = pd.Series(data2, index=index)  # 通过index参数指定索引
df = pd.DataFrame([series1, series2])
# 将df的索引设置为1开始的数字
df.index = [1, 2]
print(df)
