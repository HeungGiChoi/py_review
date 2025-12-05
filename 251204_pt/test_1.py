import numpy as np

arr = np.array([10, 20, 30, 40, 50])
# print(arr)

# print(arr[arr > 30])
# print(arr[arr % 20 == 0])

select = [0, 2, 4]
# print(arr[select])

# test
arr = np.array([-10, 20, 0, -30, 10, 50])
# print(arr)
# print(arr[arr > 0])
arr[arr < 0] = 0
# print(arr)

zeros_arrray = np.zeros((2, 3))
# print(zeros_arrray)
ones_array = np.ones((3, 2))
# print(ones_array)
test_array = np.ones((3, 2))
# print(test_array)

range_array = np.arange(1, 10, 2)
# print(range_array)
linspace_array = np.linspace(0, 1, 5)
# print(linspace_array)

zero_thounsand = np.zeros((1000, 1000))
# print(zero_thounsand.size)

# reshape() 와 resize()

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped = np.reshape(array, (3, 3))
# print(reshaped)

resized = np.resize(array, (3, 5))
# print(resized)

def make_array(n, m):
    new_array = np.arange(1, n * m + 1)
    reshape_array = np.reshape(new_array, (n, m))
    return reshape_array

# print(make_array(3, 3))

# test 3.
range_array = np.arange(1, 17)
# print(range_array)
reshaped_array = np.reshape(range_array, (4, 4))
# print(reshaped_array)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# print(a + b)

# a = np.array([1, 4, 9, 16, 25])
# sqrt_values = np.sqrt(a)
# print(sqrt_values)

# print(a + 10)
# print((a + b) / 2)

arr = np.array([-10, 20, 0, -30, 10, 50])
# print(arr * -1)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.hstack((a, b))
# print(result)

result = np.vstack((a, b))
# print(result)

result = np.column_stack((a, b))
# /print(result)
# test 4.
mid_score = np.array([90, 100, 85, 60, 75])
final_score = np.array([80, 90, 75, 50, 55])
avg_score = (mid_score + final_score) / 2

result = np.vstack((mid_score, final_score, avg_score))
# print(result)


