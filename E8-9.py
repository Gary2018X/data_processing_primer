# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********典型图制作：直方图:归一化*******#
np.random.seed(0)
data = np.random.randn(10000)

# 绘制直方图，bins指定组数,normed指定是否归一化
# 3.1版本会弃用normed，替换为density
plt.hist(data, bins=100, density=True)
plt.show()
