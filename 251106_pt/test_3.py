a = [1, 2, 3]
b = [4, 5]

print(a + b)
print(a * 2)

# 정렬 함수(리스트)
num = [2, 4, 3, 1, 8]
# num_asc = sorted(num)
# print(num_asc)
# num_desc = sorted(num, reverse=True)
# print(num_desc)

# str = ['b', 'a', 'g', 'r', 'f']
# str_asc = sorted(str)
# print(str_asc)

# str_desc = sorted(str, reverse=True)
# print(str_desc)

# num.sort()
print(num)
print(num.sort())
num.sort()
print(num)
num.sort(reverse=True)
print(num)

korean = ['강', '최', '이', '서', '임']
print(korean)
korean.sort()
print(korean)
korean.sort(reverse=True)
print(korean)

print(num)
num.reverse()
print(num)

korean.reverse()
print(korean)

print(korean.index('최'))
# print(korean.index('박'))

korean.append('박')
print(korean)
korean.pop()
print(korean)

korean.pop(0)
print(korean)

korean.remove('이')
print(korean)

korean.insert(2, '이')
print(korean)

korean.clear()
print(korean)

a = ['a', 'q', 'q', 'w', 'w', 'w', 'p']
print(a.count('w'))
