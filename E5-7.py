# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas标签参照********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

# 设置行索引标签
df.index = range(1, 11)
# 使用loc取值
df = df.loc[range(2, 6), ['banana', 'kiwifruit']]
print(df)
