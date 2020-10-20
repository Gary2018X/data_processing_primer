# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用:设置图内的表示范围********#
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

# y轴范围设为0-1
plt.ylim([0, 1])
# 可视化
plt.plot(x, y)
plt.show()
