# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化前提知识：正太分布随机********#
np.random.seed(0)
# 生成1w个符合正态分布的随机数
x = np.random.randn(10000)

# 可视化
plt.hist(x, bins='auto')
plt.show()
