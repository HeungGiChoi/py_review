# all_students = {
#     "student_1": [83, 92, 88],
#     "student_2": [90, 79, 86],
#     "student_3": [88, 86, 94]
# }
# for student, values in all_students.items():
#     print(f'{student}의 평균점수는 {sum(values)/len(values)}점 입니다.')


for i in range(2, 10):
    print(f'[{i} 단]')
    for j in range(1, 10):
        print(f'{i} X {j} = {i * j}')
    print()
