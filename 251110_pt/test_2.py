# print(abs(-7))

# def myabs(x):
#     if x < 0:
#         return -x
#     else:
#         return x

# print(myabs(-5))
# print(myabs(5))

# def square(x):
#     return x ** 2

# list_1 = [1, 2, 3, 4]
# squares = list(map(square, list_1))
# print(squares)


# numbers = [1, 2, 3, 4]

# def even_number(x):
#     return x % 2 == 0

# filters = list(filter(even_number, numbers))
# print(filters)

# 실습 4.
# def num_func(x):
#     list_2 = [i for i in range(1, 31) if i % x == 0]
#     for i in list_2:
#         print(i, end=" ")
#     print()
#     print(f'{x}의 배수의 개수: {len(list_2)}')

# num_func(5)

# 재귀함수 
# def fibonacci(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     elif x >= 2:
#         return fibonacci(x-1) + fibonacci(x-2)

# print(fibonacci(6))

## Lambda 식

# add = lambda x, y: x+y
# print(add(1, 2))

# times = lambda x: x % 2 == 0
# print(times(4))
# print(times(9))
# print((lambda x: x % 2 == 0)(9))

# def func_1(func):
#     for i in range(10):
#         func()

# hello_1 = lambda: print('hello')
# func_1(hello_1)

## test
# def calc_1(x):
#     return x * 2

# def filters(y):
#     return y > 5
# num_1 = [1, 2, 3, 4, 5]
# func_1 = tuple(filter(filters ,list(map(calc_1, num_1))))
# print(func_1)

numbers = [1, 2, 3, 4]
squares = map(lambda x: x** 2, numbers)
print(list(squares))

filters = filter(lambda x: x % 2 == 0, numbers)
print(list(filters))
