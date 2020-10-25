# -*- coding: utf-8 -*-
# author:Gary
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime

# ********典型图制作：综合练习2******#
np.random.seed(80)
X = 0  # 总得点的初始值
N = 10000  # 指定投出次数
# 描画正方形内切圆（四分之一圆）的边界线的方程式[y=V(1-x^2)(O<=x<=1)]
circle_x = np.arange(0, 1, 0.001)
circle_y = np.sqrt(1 - circle_x * circle_x)
plt.figure(figsize=(5, 5))
plt.plot(circle_x, circle_y)
start_time = datetime.datetime.now()  # 计测N次执行时的开始时间
for i in range(0, N):
    score_x = np.random.rand()  # 生成0至1之间的随机数，赋予变量score_x
    score_y = np.random.rand()  # 生成o至1之间的随机数，赋予变量score_y
    # #点(score_x,score_y）是否在圆内的判断条件
    if score_x * score_x + score_y * score_y < 1:
        plt.scatter(score_x, score_y, marker='o', color='k')  # 如果该点在圆内，则用黑色表示，否则(圆外的点)则用蓝色
        X = X + 1  # 如果该点在圆内，总得点累加1
    else:
        plt.scatter(score_x, score_y, marker='o', color='b')  # ，否则(圆外的点）则用蓝色表示
pi = 4 * float(X) / float(N)  # 计算t的近似值
# 蒙特卡洛方法计算圆周率时所花时间
end_time = datetime.datetime.now()
time = end_time - start_time
print("圆周率:%.6f" % pi)
print("花费时间:{}".format(time))
# 显示图
plt.grid(True)
plt.xlabel("X")
plt.ylabel('Y')
plt.show()
