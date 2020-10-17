# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********pandas添加数据********#
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)  # 通过index参数指定索引
series = series.append(pd.Series([12], index=['pineapple']))
print(series)
