# -*- coding: utf-8 -*-
# author:Gary
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# ********逻辑回归模型：实现******#
x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=42)
# 构建模型
model = LogisticRegression(random_state=42)
# 训练
model.fit(train_x, train_y)

# 预测
pred_y = model.predict(test_x)

# 计算并打印正确率
print(model.score(test_x, test_y))
# 生成数据可视化
plt.scatter(x[:, 0], x[:, 1], c=y, marker='.', cmap=matplotlib.cm.get_cmap(name='bwr'), alpha=0.7)

# 从学习中得到的类型分界线进行可视化
x1 = np.linspace(-10, 10)
y1 = -model.coef_[0][0] / model.coef_[0][1] * x1 - model.intercept_ / model.coef_[0][1]
plt.plot(x1, y1)
print(model.coef_)
print(model.intercept_)
print(model.coef_[0][0])
print(model.coef_[0][1])

# 调整图的比例
plt.xlim(min(x[:, 0]) - 0.5, max(x[:, 0]) + 0.5)
plt.ylim(min(x[:, 1]) - 0.5, max(x[:, 1]) + 0.5)
plt.axes().set_aspect("equal", 'datalim')

# 添加标题
plt.title("classification data using LogisticRegression")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
