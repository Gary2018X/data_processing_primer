# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd
from sklearn.model_selection import train_test_split

# ********决策树：实现******#

mush_data = pd.read_csv("agaricus-lepiota.data", header=None)

mush_data.columns = ["classes", "cap_ shape", "cap_surface",
                     "cap_color", "odor", "bruises",
                     "gill_attachment", "gill_spacing",
                     "gill_size", "gill_color", "stalk_shape",
                     "stalk_root", "stalk_surface_above_ring",
                     "stalk_surface_below_ring",
                     "stalk_color_above__ring",
                     "stalk_color_below_ring", "veil_type", "veil_color", "ring_number", "ring_type",
                     "spore_print color", "population", "habitat"]

# 对颜色的种类等不能由数值大小决定的类别型变量，变换为yes/no或0/1为属性值的虚拟(dummy) 变量
mush_data_dummy = pd.get_dummies(
    mush_data[["gill_color", "gill_attachment", "odor", "cap_color"]])
# 设立因变量flg，即在DataFrame的mush_ data_ _dummy中 添加flg列，


# 其值根据classes列中同行的值是否是"p"而赋予1或0。
mush_data_dummy["flg"] = mush_data["classes"].map(lambda x: 1 if x == "p" else 0)
# 指定自变量和因变量。即，将DataFrame的mush. _data_ dummy分为数据和类别两个部分:
X = mush_data_dummy.drop("flg", axis=1)
Y = mush_data_dummy["flg"]
# 划分训练集和测试集
train_X, test_X, train_y, test_y = train_test_split(X, Y, random_state=42)

# 从库函数/包中导入模型
from sklearn.tree import DecisionTreeClassifier

# 构建模型
model = DecisionTreeClassifier()
# 模型的学习
model.fit(train_X, train_y)
# 计算并打印正确率
print(model.score(test_X, test_y))
