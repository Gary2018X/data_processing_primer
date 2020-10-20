# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用:设置图的大小********#
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)
# 设置图的尺寸为4*4
plt.figure(figsize=(4, 4))
plt.plot(x, y)
plt.show()
