# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********典型图制作：直方图*******#
np.random.seed(0)
data = np.random.randn(10000)

# 绘制直方图
plt.hist(data)
plt.show()
