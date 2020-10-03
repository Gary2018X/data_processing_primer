# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ndarray之间的算术运算在相同位置的元素直接直接进行
arr = np.array([2, 5, 3, 4, 8])
# 相加
print(arr + arr)
# 相减
print(arr - arr)
# 三次方
print(arr ** 3)
# 1/arr
print(1 / arr)
