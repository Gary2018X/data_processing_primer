# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用:设置图内标识********#
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)
# 设置图像标题
plt.title('y=sin(x)')
# 设置x，y轴名称
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# y轴范围设为0-1
plt.ylim([0, 1])
# 可视化
plt.plot(x, y)
plt.show()
