# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********典型图制作：散点图:表示色条******#
np.random.seed(0)
x = np.random.choice(np.arange(100), 100)
y = np.random.choice(np.arange(100), 100)
z = np.random.choice(np.arange(100), 100)
# 值的大小确定标记的颜色的深浅
plt.scatter(x, y, c=z, cmap='Blues')

# 显示色条
plt.colorbar()
plt.show()
