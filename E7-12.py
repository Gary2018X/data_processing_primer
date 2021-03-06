# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用:制作子图:子图内设置标题*******#
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

# 设置图的尺寸为4*4
fig = plt.figure(figsize=(9, 6))

# 生成在从上开始的第2行、从左开始的第2列的子图
ax = fig.add_subplot(2, 3, 5)
# 图内的各个子图之间，纵横按照1的比例调整空白
plt.subplots_adjust(wspace=1, hspace=1)

# 设置子图标题
ax.set_title("y=sin(x)")
# 设置x，y轴的标题
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.plot(x, y)
for i in range(6):
    if i == 4:
        continue
    fig.add_subplot(2, 3, i + 1)

plt.show()
