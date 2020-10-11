# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********numpy综合练习2（参考了老师的代码）********#
# 模拟求解两幅图像的差分。具体地，以O-5的整数表示颜色，以ndarray二元数组表示图像，以形状相同的两个二元数组中、各个相同位置的元素的值之间的差作为新的二元数组该位置的元素的值，新的二元数组所代表的矩阵就是原来的两幅图像的差分。

np.random.seed(0)


# 生成图像
def make_image(m, n):
    image = np.random.randint(0, 6, (m, n))
    return image


# 改变一部分元素值
def change(matrix):
    shape = matrix.shape
    # 对于矩阵的各个元素随机改变值，0-5
    for i in range(shape[0]):
        for j in range(shape[1]):
            if np.random.randint(0, 2) == 1:
                matrix[i][j] = np.random.randint(0, 6, 1)
    return matrix


image1 = make_image(3, 3)
print(image1)
image2 = change(np.copy(image1))
print(image2)
# 计算差分
image3 = image2 - image1
print(image3)

# 取绝对值
image3 = np.abs(image3)
print(image3)
