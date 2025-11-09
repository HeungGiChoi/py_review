## 예제 2.
students = dict()
print(students)

students = dict(Alice=80, Bob=90, Charlie=95)
print(students)

students['David'] = 85
print(students)
students['Alice'] = 88
print(students)

del students['Bob']
print(students)