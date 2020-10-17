# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********pandas添加列数据********#
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
series1 = pd.Series(data1, index=index)  # 通过index参数指定索引
series2 = pd.Series(data2, index=index)  # 通过index参数指定索引
df = pd.DataFrame([series1, series2])
new_column = pd.Series([15, 7], index=[0, 1])
# 添加列数据
df['mango'] = new_column
print(df)
