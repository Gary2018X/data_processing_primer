# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********典型图制作：散点图:值的大小确定标记的大小******#
np.random.seed(0)
x = np.random.choice(np.arange(100), 100)
y = np.random.choice(np.arange(100), 100)
z = np.random.choice(np.arange(100), 100)
# 值的大小确定标记的大小
plt.scatter(x, y, s=z)
plt.show()
