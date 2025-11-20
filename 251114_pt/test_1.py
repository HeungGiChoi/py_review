# 클래스 복습
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f'{self.name}가 소리를 냅니다.')
    
#     def move(self):
#         print(f'{self.name}이 움직입니다.')
    
# # 자식 클래스
# class Dog(Animal):
#     def __init__(self, name, sound):
#         super().__init__(name)
#         self.sound = sound

#     def bark(self):
#         print(f'{self.name}가 {self.sound} 짖습니다.')

# dog = Dog("백구", '멍멍')
# dog.speak()
# dog.move()
# dog.bark()

## 다중 상속
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

class Car(Engine, Wheels):
    def __init__(self, horsepower, wheel_count):
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, wheel_count)

    def info(self):
        print(f'이 자동차는 {self.horsepower} 마력 엔진과 {self.wheel_count}개의 바퀴를 가지고 있습니다.')
    
car = Car(150, 4)
car.info()
# print(Car.mro())