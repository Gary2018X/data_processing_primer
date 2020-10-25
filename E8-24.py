# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
import matplotlib.pyplot as plt

# ********典型图制作：综合练习1******#
# 获取iris数据集
df_iris = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
df_iris.columns = ["sepal length", "sepal width", "petal length", " petal width", "class"]
fig = plt.figure(figsize=(10, 10))
# 描画setosa的sepal length - sepal width的关系图;#指定标签为setosa、颜色为black
plt.scatter(df_iris.iloc[:50, 0], df_iris.iloc[:50, 1], label="setosa", color="k")

# 指定标签为versicolor、颜色为blue
plt.scatter(df_iris.iloc[50:100, 0], df_iris.iloc[50:100, 1], label="versicolor", color="b")
# 描画virginica的sepal length - sepal width的关系图;
# 指定标签为virginica、颜色为green
plt.scatter(df_iris.iloc[100:150, 0], df_iris.iloc[100:150, 1], label="virginica", color="g")
# x轴名为sepal length
plt.xlabel("sepal length")
# y轴名为sepal width
plt.ylabel("sepal width")
# #画图

plt.legend(loc="best")
plt.grid(True)
plt.show()
