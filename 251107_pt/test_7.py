# 예제 1.
# gugudan = int(input('몇 단을 출력할까요?: '))
# for i in range(1, 10):
#     print(f'{gugudan} x {i} = {gugudan * i}')

# 예제 2.
# input_num = int(input('어디까지 계산할까요?: '))
# total = 0
# for i in range(1, input_num + 1):
#     if i % 2 == 1:
#         total += i
# print(f'1부터 {input_num}까지의 홀수의 합: {total}')

all_student = {
    "student_1": {
        "국어": 83,
        "영어": 92,
        "수학": 88
    },
    "student_2": {
        "국어": 90,
        "영어": 79,
        "수학": 86
    },
    "student_3": {
        "국어": 88,
        "영어": 86,
        "수학": 94
    } 
}
for key in all_student:
    