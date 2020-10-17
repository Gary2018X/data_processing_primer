# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas删除行或者列********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

# 设置行索引标签
df.index = range(1, 11)
# 使用drop方法保留奇数行
df = df.drop(np.arange(2, 11, 2))

# 使用drop删除strawberry列
df = df.drop("strawberry", axis=1)
print(df)
