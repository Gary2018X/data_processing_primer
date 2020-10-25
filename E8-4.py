# -*- coding: utf-8 -*-
# author:Gary
import matplotlib.pyplot as plt

# ********典型图制作：柱形图：设置标签*******#
x = [1, 2, 3, 4, 5, 6]
y = [12, 41, 32, 36, 21, 17]
labels = ['apple', 'orange', 'banana', 'pineapple', 'kiwifruit', 'strawberry']
# 绘制柱形图,tick_label指定x标签
plt.bar(x, y, tick_label=labels)
plt.show()
