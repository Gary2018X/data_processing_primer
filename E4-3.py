# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# 1. 观察list切片进行赋值的操作
arr_list = [x for x in range(10)]

print("arr_list", arr_list)
arr_list_copy = arr_list[:]  # 取所有内容
print("arr_list_copy", arr_list_copy)
arr_list_copy[0] = 100

print("由于list的切片被复制，arr_list中没有反应出arr_list_copy的变化")
print("arr_list", arr_list)

# 2. 观察numpy中ndarray切片进行赋值的操作
arr_numpy = np.arange(10)
print("arr_numpy", arr_numpy)
arr_numpy_view = arr_numpy[:]
print("arr_numpy_view", arr_numpy_view)

arr_numpy_view[0] = 100

print("由于numpy的切片部分的指针被赋值到arr_numpy_view,arr_numpy_view的变化也会影响原本的arr_numpy")
print("arr_numpy", arr_numpy)


# 理论上如果是指针被复制，那应该只是影响上一次操作，如果切片赋值2次，原本的数组应该不会变化。
# 两次slice操作之后赋值不会影响到原数数组，其实是是只影响最近的一次切片操作。
A = np.random.random((4, 3))
print(A)
a = A[:, [0, 1]]
print(a)
x = np.array([1.0, 2.0, 3.0, 4.0]).reshape(-1, 1)
a[:, 0:1] = x
print(a)
print(A)

# 3. 使用numpy的ndarray的copy()方法,观察对ndarray的切片进行赋值时候的表现
arr_numpy2 = np.arange(10)
print("arr_numpy2", arr_numpy2)

arr_numpy_copy = arr_numpy2[:].copy()
print("arr_numpy_copy", arr_numpy_copy)

arr_numpy_copy[0] = 100

print("使用numpy的ndarray的copy()方法时候，由于数据部分被复制，arr_numpy_copy的变化不会对arr_numpy产生影响")
print("arr_numpy2", arr_numpy2)
