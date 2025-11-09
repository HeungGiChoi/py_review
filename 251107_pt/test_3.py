## 삼항 연산자
# age = int(input('나이를 입력하세요: '))
# message = '성인입니다.' if age > 19 else '미성년자 입니다.'
# print(message)

# 리스트, 튜플, 딕셔너리 활용 if문
# fruit = input('과일을 입력하세요 : ')
# if fruit in ['사과', '멜론', '수박']:
#     print(f'입력한 과일은 {fruit} 입니다.')
# else:
#     print('존재하지 않는 과일입니다.')

## 예제 1.
fruit_cal = {
    'apple': 95,
    'melon': 102,
    'watermelon': 40,
    'grape': 120 
}
fruit_input = input('과일을 영문으로 입력하세요: ')
if fruit_input in fruit_cal:
    print(f'{fruit_input}의 칼로리는 {fruit_cal[fruit_input]}kcal입니다.')
else:
    print('존재하지 않는 과일입니다.')
