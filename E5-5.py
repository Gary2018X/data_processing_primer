# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********pandas添加行数据********#
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
data3 = [30, 12, 10, 8, 25, 3]
series1 = pd.Series(data1, index=index)  # 通过index参数指定索引
series2 = pd.Series(data2, index=index)  # 通过index参数指定索引
df = pd.DataFrame([series1, series2])
index.append('pineapple')
series3 = pd.Series(data3, index=index)
df = df.append(series3, ignore_index=True)  # 忽略索引
print(df)
