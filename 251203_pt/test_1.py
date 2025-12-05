import numpy as np

# x = np.array([3, 1, 2])
# print(x)
# print(type(x))

array_1d = np.array([1, 2, 3, 4, 5])
# 1차원 배열
# print(array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# 2차원 배열
# print(array_2d)

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# 3차원 배열
# print("3차원 배열: \n", array_3d)

array_list = [array_1d, array_2d, array_3d]

# shape
# for i in array_list:
#     print(i.shape)

# ndim
# for i in array_list:
#     print(i.ndim)

# dtype
# for i in array_list:
#     print(i.dtype)

# itemsize
# for i in array_list:
#     print(i.itemsize)

# size
# for i in array_list:
#     print(i.size)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr)

# print(arr[1, 2])
# arr[1, 2] = 120
# print(arr[1, 2])
# print(arr)

# print(arr[2])
# print(arr[2, :])
# arr[2] = 1
# print(arr)

# print(arr[:, 2])
# arr[:, 2] = 0
# print(arr)

arr[1, :] = 100
# print(arr)
arr[:, 1] = -100
print(arr)
