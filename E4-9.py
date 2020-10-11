# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组索引参照和切片********#
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
# (1)取出值为3的元素;
print(arr[0, 2])
# (2)取出二元数组[[4,5],[7,8]];
print(arr[1:, 0:2])
