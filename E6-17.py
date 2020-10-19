# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
# 生成一万个o至1之间的随机数，赋予给变量random_number_1
random_number_1 = np.random.rand(10000)
# 生成一万个o至1之间符合正态分布的随机数，赋予给变量random_number_2
random_number_2 = np.random.randn(10000)
# 生成一万个o至1之间符合二项分布的随机数，赋予给变量random_number_3，成功概率设置为0.5
random_number_3 = np.random.binomial(100, 0.5, size=10000)

plt.figure(figsize=(5, 5))
# 使用直方图表示random_number_1，bins指定为50:
plt.hist(random_number_1, bins=50)
plt.title('uniform_distribution')
plt.grid(True)
plt.show()

plt.figure(figsize=(5, 5))
# 使用直方图表示random_number_2，bins指定为50;
plt.hist(random_number_2, bins=50)
plt.title('normal_distribution')
plt.grid(True)
plt.show()

plt.figure(figsize=(5, 5))
# 使用直方图表示random_number_3，bins指定为50:
plt.hist(random_number_3, bins=50)
plt.title('binomial_distribution')
plt.grid(True)
plt.show()
