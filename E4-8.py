# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy二元数组入门********#
# (1)通过在变量arr中赋值[1,2,3,4]和[5,6,7,8]生成ndarray的二元数组;
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)
# (2)打印arr矩阵的行数和列数;
print(arr.shape)
# (3)将变量arr变换为4行2列的矩阵并予以显示;
print(arr.reshape(4, 2))
