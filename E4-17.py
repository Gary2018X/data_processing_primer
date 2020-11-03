# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy综合练习1********#
# (1)生成元素值为整数O-29的5x3矩阵，赋值给变量arr
np.random.seed(100)  # 保证随机结果一样
arr = np.random.randint(0, 30, (5, 3))
print("原二元数组：", arr)
# (2)将arr转置
# 老师的意思是arr转置后要赋值给原矩阵
arr = arr.T
# print(np.transpose(arr))
print("转置后的二元数组：", arr)
# (3)抽取arr矩阵中的第2、3、4列构成一个新的矩阵arr1
arr1 = arr[:, 1:4]
print(arr1)
# (4)对矩阵变数arr1按行排序
# np.sort(arr1)
# axis：数组排序时的基准，a x i s = 0 axis=0axis=0，按列排列；a x i s = 1 axis=1axis=1，按行排列
arr1.sort(1)
print("按行排序：", arr1)
# (5)输出arr1各列的平均值
print("各列平均值", arr1.mean(axis=0))
