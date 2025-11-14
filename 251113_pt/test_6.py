# getter / setter, 데코레이터

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value


p1 = Person("최흥기", 32)
p2 = Person("임유연", 27)

print(p1.name)
print(p1.age)

p1.name = '김철수'
p1.age = 20
print(p1.name)
print(p1.age)