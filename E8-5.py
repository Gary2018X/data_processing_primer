# -*- coding: utf-8 -*-
# author:Gary
import matplotlib.pyplot as plt

# ********典型图制作：柱形图：堆积*******#
x = [1, 2, 3, 4, 5, 6]
y1 = [12, 41, 32, 36, 21, 17]
y2 = [43, 1, 6, 17, 17, 9]
labels = ['apple', 'orange', 'banana', 'pineapple', 'kiwifruit', 'strawberry']
# 绘制柱形图,tick_label指定x标签
plt.bar(x, y1, tick_label=labels)
plt.bar(x, y2, bottom=y1)
plt.legend(('y1', 'y2'))
plt.show()
