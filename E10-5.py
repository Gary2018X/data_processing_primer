# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
from numpy import nan as NA
import pandas as pd

# ********使用pandas填充缺失值(平均值)******#
sample_data = pd.DataFrame(np.random.rand(10, 4))

# 删除一部分数据
sample_data.iloc[1, 0] = NA
sample_data.iloc[2, 2] = NA
sample_data.iloc[5:, 3] = NA
print(sample_data)

# 缺失值填充上面的值,不指定就是列平均,可以通过axis指定行还是列
sample_data1 = sample_data.fillna(sample_data.mean(axis=1))  # 列平均
sample_data2 = sample_data.fillna(sample_data.mean(axis=0))  # 行平均
print(sample_data1)
print(sample_data2)
