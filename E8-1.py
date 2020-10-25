# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********典型图制作：折线图：数据标记和颜色*******#
days = np.arange(1, 11)
weight = np.array([10, 14, 18, 20, 18, 16, 17, 18, 20, 17])

# 设置各种显示
plt.ylim([0, weight.max() + 1])
plt.xlabel('days')
plt.ylabel('weight')

# 使用黑色的圆数据标记折线
plt.plot(days, weight, marker='o', markerfacecolor='k')

plt.show()
