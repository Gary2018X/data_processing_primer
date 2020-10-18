# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

index = ['Zhang3', 'Li4', 'Wang5', 'Zhao6', 'Qian7']
columns = ['语文', '数学', '社会', '理科', '英语']
data = [[30, 45, 12, 45, 87], [65, 47, 83, 17, 58], [64, 63, 86, 57, 46, ], [38, 47, 62, 91, 63], [65, 36, 85, 94, 36]]

df = pd.DataFrame(data, index=index, columns=columns)
# df中添加新的列，列标签为"体育"，数据来自变量pe_column;
pe_column = pd.Series([56, 43, 73, 82, 62], index=index)
df["体育"] = pe_column
print(df)

# 按照数学成绩的升序排列，并赋予给df1;
df1 = df.sort_values(by="数学", ascending=True)
print(df1)

# df1的各个元素值增加5分;
df2 = df1 + 5
print(df2)

# 计算df的摘要统计量，并输出"mean"、"max"、 "min";
print(df2.describe().loc[["mean", "max", "min"]])
