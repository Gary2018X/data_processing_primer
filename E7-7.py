# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用:设置图内标识********#
x = np.linspace(0, 2 * np.pi)
y1 = np.sin(x)
y2 = np.cos(x)
positions = [np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2]
labels = ["90°", "180° ", "270°", "360°"]
plt.title("graphs of trigonometric functions")
# 设置x，y轴名称
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
# 在x轴上设置刻度
plt.xticks(positions, labels)
plt.plot(x, y1, color='k', label='y=sin(x)')
plt.plot(x, y2, color='c', label='y=cos(x)')
plt.legend()  # 让图例生效
plt.show()
