# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas DataFrame对数据进行摘要统计********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
# 查看所有的摘要统计量
print(df.describe())
df_des = df.describe().loc[['mean', 'max', 'min']]
print(df_des)
