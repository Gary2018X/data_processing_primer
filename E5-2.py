# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********pandas索引********#
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)  # 通过index参数指定索引
# 通过索引参照的方式获取
item1 = series[1:4]
print(item1)
# 通过指定标签的方式获取
item2 = series[['apple', 'banana', 'kiwifruit']]
print(item2)
