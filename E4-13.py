# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组转置和排序********#
arr = np.array([[8, 4, 2], [3, 5, 1]])
# 转置，作业没有要求，记录一下
print(np.transpose(arr))
print(arr.T)
# argsort()方法:机器学习中常用，返回的是排序完毕数组的元素的下标;
print("np.argsort()", np.argsort(arr))

# np.sort():与sort()方法一样，但返回排序完毕的数组的复制;
print("np.sort()", np.sort(arr))

# sort()方法:参数为O时，按列对同行的元素进行排序，参数为1时，按行对同一列的元素进行排序;,返回值为空
arr.sort()
print("sort()", arr)
