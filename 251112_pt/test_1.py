# 클래스
# class Car:
#     model = ""
#     cc = 0

# car1 = Car() # 인스턴스 생성
# car1.model = '아반떼'
# car1.cc = 1600

# car2 = Car() # 인스턴스 생성
# car2.model = 'K5'
# car2.cc = 2000

# print(f'모델명 : {car1.model}')
# print(f'배기량 : {car1.cc}cc')
# print(f'모델명 : {car2.model}')
# print(f'배기량 : {car2.cc}cc')

# class Car:
#     model = ""
#     cc = 0

#     def get_info(self):
#         print(f"모델명 : {self.model}, 배기량 : {self.cc}cc")

# car1 = Car() # 인스턴스 생성 / 객체 생성
# car1.model = '아반떼'
# car1.cc = 1600
# car1.get_info()

class Car:

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def get_info(self):
        print(f'모델명 : {self.model}, 연식 : {self.year}년형')

    def __str__(self):
        return f'모델명 : {self.model}, 연식 : {self.year}년형'

car1 = Car('BMW', 2024) # 인스턴스 생성
car1.get_info()

car2 = Car('K5', 2013)
car2.get_info()

car3 = Car('sm3', 2019)
print(car3)

cars = [
    Car('BENZ', 2018),
    Car('Audi', 2025),
    Car('porshew', 2024)
]

for car in cars:
    print(car)

