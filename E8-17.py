# -*- coding: utf-8 -*-
# author:Gary

import matplotlib.pyplot as plt

# ********典型图制作：饼图:设置标签******#
data = [60, 20, 10, 5, 3, 2]
labels = ['apple', 'orange', 'banana', 'pineapple', 'kiwifruit', 'strawberry']
# 制图饼图,labels指定标签
plt.pie(data, labels=labels)
# 椭圆变正圆
plt.axis('equal')
plt.show()
