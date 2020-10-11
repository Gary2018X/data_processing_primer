# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy全局函数********#
arr = np.array([4, -9, 16, -4, 20])
# #将变量arr中各个元素的值的绝对值赋予变量arr_abs;
arr_abs = np.abs(arr)
print(arr_abs)
# 输出变量arr_abs的e次方
print(np.exp(arr_abs))
# 输出arr_abs的平方根
print(np.sqrt(arr_abs))
