t1 = (1,)

print(t1)

# 튜플 자료형은 () 생략 가능
t2 = 1, 2, 3
print(t2)

# 세트(set)
s1= {1, 2, 3, 4, 5}
print(s1)
s2 = set((1, 2, 3, 4, 5))
print(s2)
s3 = set([1, 2, 3, 4, 5])
print(s3)
s4 = {'가', '나', '나', '다', '라', '라', '마', '가'}
print(s4)

s5 = {1, 2, 3, 4, 5}
s5.add(7)
print(s5)
# s5.add([4, 5, 6, 7, 8])
# print(s5)
s5.update([4, 5, 6, 7, 8])
print(s5)

s5.remove(8)
print(s5)
# s5.remove([1, 2, 3])
# print(s5)
# s5.discard([1, 2, 3])
# print(s5)
s5.remove(1)
print(s5)

s5.clear()
print(s5)

print(s4)

s6 = s3 | s4
print(s6)

s6 = s3 & s4
print(s6)

s6 = s3 - s4
print(s6)