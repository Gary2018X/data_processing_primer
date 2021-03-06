# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用:制作子图********#
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)
# 设置图的尺寸为4*4
fig = plt.figure(figsize=(9, 6))

# 生成在从上开始的第2行、从左开始的第2列的子图
ax = fig.add_subplot(2, 3, 5)

ax.plot(x,y)
for i in range(6):
    if i == 4:
        continue
    fig.add_subplot(2, 3, i + 1)

plt.show()
