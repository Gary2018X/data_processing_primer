# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组统计函数********#
arr = np.arange(15).reshape((3, 5))
print(arr)
# 按列计算变量arr的平均值
# print(np.average(arr))
# print(np.mean(arr))
print(arr.mean(axis=0))
# 按行计算变量arr的和
# print(np.sum(arr))
print(arr.sum(axis=1))
# 变量arr的最小值
print(np.min(arr))
print(arr.min())
# 输出变量arr中各列的最大值的索引号
# print(np.argmax(arr))
print(arr.argmax(axis=0))
# 补充：标准方差np.std(),分布np.var()等
print(np.std(arr))
print(np.var(arr))
