## 내장 함수
num = [10, 20, 30, 40, 50]
result = sum(num)
print(result)

# num = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# result = sum(num.values())
# print(result)

## max, min
result = max(num)
print(result)

result = min(num)
print(result)


num = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
result = max(num.values())
print(result)

## len

num_2 = [10, 20, 30, 40]
print(len(num_2))

names = ['Alice', 'Bob', 'cris']
values = [80, 95, 50]
zipped = list(zip(names, values))
print(zipped)