## 조건문
## for
# age = 15
# if age > 20:
#     print("나는 성인 입니다.")
# elif age < 20:
#     print("나는 미성년자 입니다.")

# print(f'나이는 {age}세 입니다.')

## 예제
# password = input('비밀번호를 입력하세요: ')
# if password == 'abc123':
#     print('비밀번호가 맞습니다.')
# else:
    # print('비밀번호가 틀렸습니다.')

# num = int(input('숫자를 입력하세요: '))
# if num % 2 == 0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')

# age = int(input('나이를 입력하세요: '))
# if age < 20:
#     print('미성년자 입니다.')
# elif age > 20 and age < 30:
#     print('20대 입니다.')
# elif age > 30 and age < 40:
#     print('30대 입니다.')
# elif age > 40 and age < 50:
#     print('40대 입니다.')

# score = int(input('점수를 입력하세요: '))
# if score < 60:
#     print('학점: F')
# elif score >= 60 and score < 70:
#     print('학점 : D')
# elif score >= 70 and score < 80:
#     print('학점 : C')
# elif score >= 80 and score < 90:
#     print('학점 : B')
# elif score >= 90:
#     print('학점 : A')

## 예제 2.

age = int(input('나이를 입력해주세요: '))

if age < 8 or age >= 75:
    print(f'{age}세의 요금은 무료 입니다.')
elif age >= 8 and age < 14:
    print(f'{age}세의 요금은 450원 입니다.')
elif age >= 14 and age < 20:
    payment = input('결제방식을 선택해주세요(현금 또는 카드): ')
    if payment == '카드':
        print(f'{age}세의 {payment} 요금은 720원 입니다.')
    elif payment == '현금':
        print(f'{age}세의 {payment} 요금은 1000원 입니다.')
elif age >= 20 and age < 75:
    payment = input('결제방식을 선택해주세요(현금 또는 카드): ')
    if payment == '카드':
        print(f'{age}세의 {payment} 요금은 1200원 입니다.')
    elif payment == '현금':
        print(f'{age}세의 {payment} 요금은 1300원 입니다.')

