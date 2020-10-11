# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组广播机制********#
# 使用由O-4整数值构成的narray数组y，将一个3x5的ndarray数组x的各个元素的值减去所在列的索引号（最左列是第0列）。
x = np.arange(15).reshape((3, 5))
print(x)
y = np.array([np.arange(5)])
print(y)
z = x - y
print(z)
