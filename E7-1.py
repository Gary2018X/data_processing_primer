# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用********#
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

plt.plot(x, y)
plt.show()
