# 인스턴스 변수와 클래스 변수

class Dog:
    kind = "진돗개"

    def __init__(self, name):
        self.name = name

dog1 = Dog("백구")
dog2 = Dog("시고르자브")

print(dog1.name)
print(dog2.name)

print(dog1.kind)
print(dog1.kind)
print(Dog.kind)

class Example:
    shared = "공유 변수"

    def __init__(self, name):
        self.name = name

e1 = Example("A")
e2 = Example("B")

Example.shared = "변경된 공유 변수"

print(e1.shared)
print(e2.shared)

print(e1.name)
print(e2.name)

e1.name = "C"
e2.name = "Z"

print(e1.name)
print(e2.name)