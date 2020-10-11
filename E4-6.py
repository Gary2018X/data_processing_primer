# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy集合运算********#
arr1 = np.array([2, 5, 7, 9, 5, 2])
arr2 = np.array([2, 5, 8, 3, 1])
# (1)使用np.unique()方法，去除变量arr1中的重复元素，赋值给变量new_arr1;
new_arr1 = np.unique(arr1)
print(new_arr1)
# (⑵输出变量new_arr1和变量arr2的并集运算结果;
print(np.union1d(new_arr1, arr2))
# (3输出变量new_arr1和变量arr2的交集运算结果;
print(np.intersect1d(new_arr1, arr2))
# (4)输出变量new_arr1和变量arr2的差集运算结果;
print(np.setdiff1d(new_arr1, arr2))
# (5)使用setxor1d输出x和y的异或集
print(np.setxor1d(new_arr1, arr2))
