# -*- coding: utf-8 -*-
# author:Gary
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

from sklearn.datasets import make_gaussian_quantiles

# ********非线性SVM：实现******#
x, y = make_gaussian_quantiles(n_samples=1000, n_classes=2, n_features=2, random_state=42)

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=42)
# 构建模型
model1 = SVC()
model2 = LinearSVC()
# 训练
model1.fit(train_x, train_y)
model2.fit(train_x, train_y)

# 计算并打印正确率
print("非线性SVM正确率：", model1.score(test_x, test_y))
print("线性SVM正确率：", model2.score(test_x, test_y))
