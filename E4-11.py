# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组整数数组索引********#
# 从数组arr1中，按照行索引[o,0]和[2,3]、列索引[o,2]和[0,1]，请补充打印语句并写出取出的数组arr2。
arr1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(arr1)
rows1 = np.array([[0, 0], [2, 3]])
cols1 = np.array([[0, 2], [0, 1]])
arr2 = arr1[rows1, cols1]
print('数组arr2的四个元素是:')
print(arr2)
