# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用:设置自定义刻度********#
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)
# 设置图像标题
plt.title('y=sin(x)')
# 设置x，y轴名称
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# 设置网格线
plt.grid(True)
positions = [0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2]
labels = ["O ", "90°", "180° ", "270°", "360°"]
# 在x轴上设置刻度
plt.xticks(positions, labels)
# 可视化
plt.plot(x, y)
plt.show()
