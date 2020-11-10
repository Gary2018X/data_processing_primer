# -*- coding: utf-8 -*-
# author:Gary
import matplotlib.pyplot as plt
import numpy as np

# ********典型图制作：柱形图：堆积*******#
x = [1, 2, 3, 4, 5, 6]
y1 = np.array([12, 41, 32, 36, 21, 17])
y2 = np.array([43, 1, 6, 17, 17, 9])
y3 = np.array([23, 20, 16, 8, 8, 26])
labels = ['apple', 'orange', 'banana', 'pineapple', 'kiwifruit', 'strawberry']
# 绘制柱形图,tick_label指定x标签
plt.bar(x, y1, tick_label=labels)
plt.bar(x, y2, bottom=y1)
plt.bar(x, y3, bottom=y1 + y2)
plt.legend(('y1', 'y2', 'y3'))
plt.show()
