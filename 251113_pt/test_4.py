# 정보은닉
class Person:
    def __init__(self):
        self._name = ""  # 멤버 변수 초기화
        self._age = 0

    def setname(self, name):
        self._name = name
    
    def getname(self):
        return self._name
    
    def setage(self, age):
        self._age = age

    def getage(self):
        return self._age
    
p1 = Person()
p1.setname("흥부")
p1.setage(35)
print("이름 : ", p1.getname())
print("나이 : ", p1.getage())

p2 = Person()
p2.setname("놀부")
p2.setage(38)
print("이름 : ", p2.getname())
print("나이 : ", p2.getage())