# -*- coding: utf-8 -*-
# author:Gary

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# ********综合练习******#
x, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, random_state=0)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)
# 构建模型
model_list = {"逻辑回归模型": LogisticRegression(),
              "线性SVM": LinearSVC(),
              "非线性SVM": SVC(),
              '决策树': DecisionTreeClassifier(),
              '随机森林': RandomForestClassifier()}

# 使用for语句，执行模型的学习、预测并打印正确率
for model_name, model in model_list.items():
    # 模型的学习
    model.fit(train_x, train_y)
    print(model_name)
    # 预测并打印正确率
    print('正确率: ' + str(model.score(test_x, test_y)))
    print()
