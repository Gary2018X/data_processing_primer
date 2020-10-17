# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas过滤********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

# 设置行索引标签
df.index = range(1, 11)
print(df)

df = df.loc[df['apple'] >= 5][df['kiwifruit'] >= 4]
print(df)
