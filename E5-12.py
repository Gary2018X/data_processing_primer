# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas series和dataframe综合练习********#
index = ['growth', 'mission', 'zhangsan', 'pro']
data = [50, 7, 26, 1]
# 生成series
series = pd.Series(data, index=index)
# 按照索引升序排列
aidemy = series.sort_index()
print(aidemy)
# 增加元素
aidemy1 = pd.Series([30], index=['tutor'])
aidemy2 = series.append(aidemy1)
print(aidemy2)

df = pd.DataFrame()
for i in index:
    df[i] = np.random.choice(range(1, 11), 10)

# 设置行索引标签
df.index = range(1, 11)
print(df)

# 使用loc获取数据
aidemy3 = df.loc[range(2, 6), ['zhangsan']]
print(aidemy3)
