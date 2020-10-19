# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********可视化前提知识：列表中随机********#
x = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']
np.random.seed(0)
# 从x中随机5个
y = np.random.choice(x, 5)
print(y)
