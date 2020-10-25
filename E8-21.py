# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ********典型图制作：3D图:3D直方图******#
# 生成Figure对象
fig = plt.figure(figsize=(5, 5))
# 生成子图ax
ax = fig.add_subplot(111, projection="3d")
# 决定x、 y、z的位置
xpos = [i for i in range(10)]
ypos = [i for i in range(10)]
zpos = np.zeros(10)
# 决定x、y、z的变化量
dx = np.ones(10)
dy = np.ones(10)
dz = [i for i in range(10)]
# 制作3D直方图
ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
plt.show()
