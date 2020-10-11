# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
# 直接导入ranint方法
from numpy.random import randint

# ********numpy随机数********#
# (2)生成5x2矩阵的整数随机数，值大于O但不大于11，赋值给变量arr1;

# 随机生成在x以上y以下整数区间值中的z个整数的np.random.randint(x, y, z)方法,其中，z可以以“(n,m)”等形式表达生成n行m列的随机数矩阵。

arr1 = randint(0, 11, (5, 2))
print(arr1)
# (3)生成三个0至1之间的小数随机数，赋值给变量arr2:
# 随机生成o以上1以下区间值z个的np.random.rand(z)
arr2 = np.random.rand(3)
print(arr2)
# (4)随机生成符合高斯分布的np.random.normal()方法等;
'''
参数loc(float)：正态分布的均值，对应着这个分布的中心。
参数scale(float)：正态分布的标准差
参数size(int 或者整数元组)：输出矩阵的shape，默认为None。
'''
arr3 = np.random.normal(loc=0, scale=0.1, size=100)
print(arr3)
# 检验均值和方差
print(abs(0 - np.mean(arr3)) < 0.01, abs(0.1 - np.std(arr3, ddof=1)) < 0.01)
