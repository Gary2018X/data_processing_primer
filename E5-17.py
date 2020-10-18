# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas DataFrame对数据进行计算********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

# 各个元素乘以2
double_df = df * 2
print(double_df)
# 各个元素平方
square_df = df * df
print(square_df)
# 各个元素平方根
sqrt_df = np.sqrt(df)
print(sqrt_df)
