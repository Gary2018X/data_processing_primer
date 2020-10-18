# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

df1 = pd.DataFrame([['apple', 'Fruit', 120], ['orange', 'Fruit', 60], ['banana', 'Fruit', 100],
                    ['pumpkin', 'Vegetable', 150], ['potato', 'Vegetable', 80]], columns=['Name', 'Type', 'Price'])

df2 = pd.DataFrame([['onion', 'Vegetable', 60], ['carrot', 'Vegetable', 50], ['beans', 'Vegetable', 100],
                    ['grape', 'Fruit', 160], ['kiwifruit', 'Fruit', 80]], columns=['Name', 'Type', 'Price'])

# 结合
df3 = pd.concat([df1, df2], axis=0)
print(df3)
# 抽取水果数据并按价格排序
df_fruit = df3.loc[df3['Type'] == 'Fruit']
df_fruit = df_fruit.sort_values(by='Price')
print(df_fruit)
# 抽取蔬菜数据按照价格排序
df_veg = df3.loc[df3['Type'] == 'Vegetable']
df_veg = df_veg.sort_values(by='Price')
print(df_veg)

# 分别U型俺去最低价格的三种，计算六中物品的合计价格
print(sum(df_fruit[:3]['Price']) + sum(df_veg[:3]['Price']))
