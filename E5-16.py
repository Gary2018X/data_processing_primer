# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas DataFrame取得部分行********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

# 取得df的前三行
df_head = df.head(3)
print(df_head)
# 取得df的后三行
df_tail = df.tail(3)
print(df_tail)
