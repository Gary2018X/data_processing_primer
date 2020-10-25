# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********典型图制作：直方图:堆积*******#
np.random.seed(0)
data = np.random.randn(10000)

# 绘制直方图，bins指定组数,normed指定是否归一化,cumulative指定是否堆积
plt.hist(data, bins=100, normed=True, cumulative=True)
plt.show()
