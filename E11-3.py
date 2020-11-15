# -*- coding: utf-8 -*-
# author:Gary
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import matplotlib

# ********有监督的学习：准备数据******#

# n_samples样本数, n_features特征个数,n_redundant冗余信息
x, y = make_classification(n_samples=50, n_features=2, n_redundant=0, random_state=0)

# 可视化
plt.scatter(x[:, 0], x[:,1], c=y, marker='.', cmap=matplotlib.cm.get_cmap(name='bwr'), alpha=0.7)
plt.grid(True)
plt.show()
