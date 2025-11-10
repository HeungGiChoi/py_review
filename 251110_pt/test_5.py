# def solution(array, n):
#     answer = [i for i in array if i == n]
#     return len(answer)

# array_1 = [1, 2, 3, 4, 5, 2, 1, 1]
# print(array_1.count(1))

# a = 3.5
# print(round(a))

# def solution(array):
#     answer = len(array) / 2
#     return round(answer)

# array_1 = [1, 2, 3]
# print(solution(array_1))

array_1 = [9, -1, 0]
array_1.sort()
middle_value = round(len(array_1) / 2)
print(array_1[middle_value - 1])
    