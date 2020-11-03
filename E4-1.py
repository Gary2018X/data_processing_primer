# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

storages = [24, 3, 4, 23, 10, 123]
print(storages)

# 1. 调用array方法生成ndarray
# np.array(list数据类型)
np_storages = np.array(storages)
print(np_storages, type(np_storages))


# 2. 调用arange方法生成ndarray
# np.arange(X)生成0至X-1个整数的一元数组
# np.arange(4)  # 生成[0,1,2,3]
