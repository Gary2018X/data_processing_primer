# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy布尔值索引********#
arr = np.array([2, 3, 4, 5, 6, 7])
# (1)打印变量arr的各个元素是否能被2整除的布尔值数组;
print(arr % 2 == 0)
# (2)变量arr的各个元素中，打印能被2整除的元素的数组;
print(arr[arr % 2 == 0])
