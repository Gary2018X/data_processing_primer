# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组矩阵计算********#
arr = np.arange(9).reshape((3, 3))
# np.dot(a,b)方法:两个矩阵a和b之间的乘积运算;
print(np.dot(arr, arr))
# np.linalg.norm(a):计算矩阵a的范数;
vec = arr.reshape(9)
print(np.linalg.norm(vec))
