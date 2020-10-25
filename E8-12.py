# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********典型图制作：散点图:设置颜色和标记******#
np.random.seed(0)
x = np.random.choice(np.arange(100), 100)
y = np.random.choice(np.arange(100), 100)

# 四角形标记和黑色
plt.scatter(x, y, marker='s', color='k')
plt.show()
