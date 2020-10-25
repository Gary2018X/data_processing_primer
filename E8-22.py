# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ********典型图制作：3D图:3D散点图******#
np.random.seed(0)

X = np.random.randn(1000)
Y = np.random.randn(1000)
Z = np.random.randn(1000)
# 生成Figure对象
fig = plt.figure(figsize=(6, 6))
# 生成子图ax
ax = fig.add_subplot(1, 1, 1, projection="3d")
# x、Y、z变量的数据转换为一维数据x、y、z变量
x = np.ravel(X)
y = np.ravel(Y)
z = np.ravel(Z)

# 制作3D散点图
ax.scatter3D(x, y, z)
plt.show()
