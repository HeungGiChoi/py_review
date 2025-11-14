# 상속
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

    def move(self):
        print("동물이 움직입니다.")

# 자식 클래스
class Dog(Animal):
    def bark(self):
        print("멍멍!")

dog = Dog()
dog.speak()
dog.move()
dog.bark()

#---------------------------------------------------
class Car:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name}이 이동합니다.')

    def crocktion(self):
        print(f'{self.name}이 크락션을 울립니다.')
    

class Kia(Car):
    def __init__(self, name, numbers):
        super().__init__(name)
        self.numbers = numbers
    
    def carnum(self):
        print(f'{self.name}의 차량번호는 {self.numbers} 입니다.')
    
car1 = Kia("K5", "145루2778")
car1.crocktion()
car1.move()
car1.carnum()
