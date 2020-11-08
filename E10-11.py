# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
from numpy import nan as NA

# ********综合练习******#
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df.columns = ['', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flacanoids',
              'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wine',
              'Proline']
# 取前10行
df_ten = df.head(10)
print(df_ten)

# 制作缺失数据
df_ten.iloc[1, 0] = NA
df_ten.iloc[2, 3] = NA
df_ten.iloc[4, 8] = NA
df_ten.iloc[7, 3] = NA
print(df_ten)

# 缺失值填充平均值
df_ten = df_ten.fillna(df_ten.mean())
print(df_ten)

# 求alcohol的平均值
print(df_ten['Alcohol'].mean())

# 制作重复行并删除
df_ten.append(df_ten.loc[3])
df_ten.append(df_ten.loc[6])
df_ten.append(df_ten.loc[9])
df_ten = df_ten.drop_duplicates()
print(df_ten)

# 离散化处理
alcohol_bins = [0, 5, 10, 15, 20, 25]
alcohol_cut_data = pd.cut(df_ten['Alcohol'], alcohol_bins)

# 汇总并打印各个区间内的数据
print(pd.value_counts(alcohol_cut_data))
