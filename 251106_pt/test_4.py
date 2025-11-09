## 예제 1.
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

print(rainbow[2])
rainbow.sort()
print(rainbow)
rainbow.append('black')
print(rainbow)
del rainbow[3:7]
print(rainbow)

## 이차원 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

value = matrix[1][1]
print(value)

matrix[2] = matrix[2] + [100]
print(matrix)

matrix = matrix + [[100, 200, 300]]
print(matrix)

del matrix[1]
print(matrix)

rows = len(matrix)
print(rows)
cols = len(matrix[1])
print(cols)

matrix.append([500, 600, 700])
print(matrix)

matrix[1].insert(1, 200)
print(matrix)

matrix = [[1, 2], [3, 4]]
matrix[0].extend([3, 4])
print(matrix)

my_list = ['a', 'b', 'c']
my_list.extend('def')
print(my_list)

# append는 리스트가 하나의 요소로 추가
my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)

# extend는 리스트의 각각 요소로 추가
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)
