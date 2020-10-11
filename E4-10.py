# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组求和********#
# 设计一个至少三行的ndarray数组，使得行的求和结果如下:[6 21 57]。
arr1 = np.array([[2, 1, 3], [7, 8, 6], [18, 20, 19]])
# 按行求和
print(arr1.sum(axis=1))
# 按列求和
print(arr1.sum(axis=0))
# 所有元素求和
print(arr1.sum())
