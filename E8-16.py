# -*- coding: utf-8 -*-
# author:Gary

import matplotlib.pyplot as plt

# ********典型图制作：饼图******#
data = [60, 20, 10, 5, 3, 2]

# 制图饼图
plt.pie(data)
# 椭圆变正圆
plt.axis('equal')
plt.show()
