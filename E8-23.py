# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# ********典型图制作：3D图:色调变化******#
t = np.linspace(-2 * np.pi, 2 * np.pi)
X, Y = np.meshgrid(t, t)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

# 生成figure
fig = plt.figure(figsize=(6, 6))

# 生成子图
ax = fig.add_subplot(1, 1, 1, projection='3d')
# 对z轴进行色调变化
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.show()
