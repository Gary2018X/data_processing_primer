# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import numpy as np

# ********pandas DataFrame对数据进行行间或者列间计算********#
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

# 计算各行与其后相隔2行的行之间的差，赋予给变量df_diff
df_diff = df.diff(-2, axis=0)
print(df)
print(df_diff)
