# -*- coding: utf-8 -*-
# author:Gary

import matplotlib.pyplot as plt

# ********典型图制作：饼图:强调特定部分******#
data = [60, 20, 10, 5, 3, 2]
labels = ['apple', 'orange', 'banana', 'pineapple', 'kiwifruit', 'strawberry']
explode = [0, 0, 0.1, 0, 0, 0]
# 制图饼图，explode指定强调内容，值的大小表名突出去多少
plt.pie(data, labels=labels, explode=explode)
# 椭圆变正圆
plt.axis('equal')
plt.show()
