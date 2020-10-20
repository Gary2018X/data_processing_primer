# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt

# ********可视化基本使用:综合练习*******#
x_upper = np.linspace(0, 5)
x_lower = np.linspace(0, 2 * np.pi)
x_tan = np.linspace(-np.pi / 2, np.pi / 2)
positions_upper = [i for i in range(5)]
positions_lower = [0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2]
positions_tan = [-np.pi / 2, 0, np.pi / 2]
labels_upper = [i for i in range(5)]
labels_lower = ["O°", "90°", "180°", "270°", "360°"]
labels_tan = ["-90° ", "O° ", "90°"]
# 生成Figure对象
fig = plt.figure(figsize=(9, 6))
# 请生成2x3布局、分别使用不同数学函数的图形

# (1)完成2x3的布局，上面一行从左至右是y=x、y=x*x、y=x*x*x，下面一行是y=sin(x)、y=cos(x)、y=tan(x)等，共计六个子图的图形;

# (2)各个子图里给出适当的标题和网格线;

# (3)准备完毕的诸变量中，带有_upper后缀的变量用于第一行的相关子图，带有_lower后缀的变量用于第二行的相关子图;但其中y=tan(x)的范围与其它子图不相同，使用_tan后缀的变量中的数据。

y_x = fig.add_subplot(2, 3, 1)
y_x.grid(True)
# 设置子图标题
y_x.set_title("y=x")
# 设置x，y轴的标题
y_x.set_xlabel("x-axis")
y_x.set_ylabel("y-axis")
y_x.plot(x_upper, x_upper)

y_xx = fig.add_subplot(2, 3, 2)
y_xx.grid(True)
# 设置子图标题
y_xx.set_title("y=x*x")
# 设置x，y轴的标题
y_xx.set_xlabel("x-axis")
y_xx.set_ylabel("y-axis")
y_xx.plot(x_upper, x_upper * x_upper)

y_xxx = fig.add_subplot(2, 3, 3)
y_xxx.grid(True)
# 设置子图标题
y_xxx.set_title("y=x*x*x")
# 设置x，y轴的标题
y_xxx.set_xlabel("x-axis")
y_xxx.set_ylabel("y-axis")
y_xxx.plot(x_upper, x_upper * x_upper * x_upper)

y_sin = fig.add_subplot(2, 3, 4)
y_sin.grid(True)
# 设置子图标题
y_sin.set_title("y=sin(x)")
# 设置x，y轴的标题
y_sin.set_xlabel("x-axis")
y_sin.set_ylabel("y-axis")
y_sinx = np.sin(x_lower)
y_sin.plot(x_lower, y_sinx)

y_cos = fig.add_subplot(2, 3, 5)
y_cos.grid(True)
# 设置子图标题
y_cos.set_title("y=cos(x)")
# 设置x，y轴的标题
y_cos.set_xlabel("x-axis")
y_cos.set_ylabel("y-axis")
y_cosx = np.cos(x_lower)
y_cos.plot(x_lower, y_cosx)

y_tan = fig.add_subplot(2, 3, 6)
y_tan.grid(True)
# 设置子图标题
y_tan.set_title("y=tan(x)")
# 设置x，y轴的标题
y_tan.set_xlabel("x-axis")
y_tan.set_ylabel("y-axis")
y_tanx = np.tan(x_tan)
y_tan.plot(x_tan, y_tanx)
plt.show()
