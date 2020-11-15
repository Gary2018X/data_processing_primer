# -*- coding: utf-8 -*-
# author:Gary
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# ********有监督的学习：学习和预测******#
x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=42)
# 构建模型
model = LogisticRegression(random_state=42)
# 训练
model.fit(train_x, train_y)

# 预测
pred_y = model.predict(test_x)
print('预测结果：', pred_y)
print('实际结果：', test_y)
