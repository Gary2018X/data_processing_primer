# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas排序********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

# 设置行索引标签
df.index = range(1, 11)
print(df)
# 按照行标签排序，对各列数据按升序排序
df = df.sort_values(by=columns)
print(df)
