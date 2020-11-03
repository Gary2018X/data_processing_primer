# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组花式索引********#
# 生成一个5x5的ndarray数组变量arr，取得该变量的第2、4、1行的元素构建新的ndarray数组。注意，“该变量的第x行”与“索引为第x行”的不同。
arr = np.arange(25).reshape((5, 5))
print(arr)
# 顺序花式索引多行
arr2 = arr[[2, 4, 1]]
print(arr2)
# 倒序花式索引多行
arr3 = arr[[-3, -1, -4]]
print(arr3)
# 取多列数据
print(arr.T[[2, 4, 1]])
