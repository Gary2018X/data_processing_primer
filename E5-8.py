# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas索引号参照********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

# 设置行索引标签
df.index = range(1, 11)

# 使用iloc方法取值,索引号从0开始
df = df.iloc[range(1, 5), [2, 4]]
print(df)
