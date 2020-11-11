# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********使用pandas按key计算平均值******#
df = pd.read_csv("wine.data", header=None)
df.columns = ['', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flacanoids',
              'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wine',
              'Proline']
print(df['Alcohol'].mean())
