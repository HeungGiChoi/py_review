## 감각 깨우기
## 리스트
# num = [3, 1, 5, 2]
# num_asc = sorted(num)
# print(num_asc)

# num_desc = sorted(num, reverse=True)
# print(num_desc)

# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'pink']
# print(rainbow[2])
# rainbow_asc = sorted(rainbow)
# print(rainbow_asc)
# rainbow.append('black')
# print(rainbow)
# del rainbow[3:6]
# print(rainbow)

# student_score = {
#     "Alice": 85,
#     "Bob": 90,
#     "Charlie": 95
# }
# student_score["David"] = 80
# # print(student_score)
# student_score["Alice"] = 88
# # print(student_score)
# del student_score["Bob"]
# print(student_score)

# score_input = int(input('점수를 입력하세요: '))
# if score_input >= 90:
#     print('학점: A')
# elif 80 <= score_input < 90:
#     print('학점: B')
# elif 70 <= score_input < 80:
#     print('학점: C')
# elif 60 <= score_input < 70:
#     print('학점: D')
# elif score_input < 60:
#     print('학점: F')

# num_input = int(input('몇단을 출력할까요?: '))
# for i in range(1, 10):
#     print(f'{num_input} x {i} = {num_input * i}')

class Practice():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b

practice = Practice(10, 2)
print(practice.add())
print(practice.sub())
print(practice.mul())
print(practice.div())


