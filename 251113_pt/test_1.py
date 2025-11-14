# 사번 자동부여 클래스
class Employee:
    # serial_num = 1000 # 기본값 (클래스 변수)

    def __init__(self, name):
        self.serial_num = 1000
        self.serial_num += 1
        self.id = self.serial_num
        self.name = name
        
    # def __init__(self, name):
    #     Employee.serial_num += 1 # serial_num을 1 증가. 사번 1000번은 존재 x. 맨 처음부터 1001번임
    #     self.id = Employee.serial_num
    #     self.name = name

    def __str__(self):
        return f'사번 : {self.id}, 이름 : {self.name}'

employee1 = Employee('최흥기')
employee2 = Employee('임유연')
employee3 = Employee('김철수')

print(employee1)
print(employee2)
print(employee3)