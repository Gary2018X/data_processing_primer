# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********pandas入门********#
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)  # 通过index参数指定索引
print(series)
