# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********可视化前提知识：固定随机********#
# 不设置seed
x = np.random.rand(5)
y = np.random.rand(5)
print('x:', x)
print('y:', y)

np.random.seed(0)  # 设置seed
x = np.random.randn(5)

np.random.seed(0)
y = np.random.randn(5)
print('x:', x)
print('y:', y)
