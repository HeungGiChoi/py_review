# while 문
num = 1
total = 0

# while num <= 10:
#     total += num
#     num += 1
# print(f'1부터 10까지의 합은 {total} 입니다.')

# user_input = ""
# while user_input != "종료":
#     user_input = input("종료하려면 '종료'를 입력하세요: ")
#     print(f'입력한 값: {user_input}')
# print('프로그램이 종료되었습니다.')

# 무한반복 탈출
# lunch = ""
# while True:
#     lunch = input('오늘의 점심메뉴는? ')
#     if lunch == '그만':
#         break
#     print(f'오늘의 점심은 {lunch} 입니다.')
# print('점심 추첨 완료')

# count = 0
# while count < 10:
#     count += 1
#     if count % 2 != 0:
#         continue
#     print(count, end=" ")

# 예제3.
# input_num = ""
while True:
    input_num = input("양수를 입력하세요 ('종료' 입력 시 프로그램 종료): ")
    num = 1
    total = 0
    if input_num.isdigit():
        if int(input_num) == 0:
            continue
        elif int(input_num) < 0:
            print('양수만 입력 하세요')
        elif int(input_num) > 0:
            while num <= int(input_num):
                total += num
                num += 1
            print(f'1부터 {input_num}까지의 합은 {total} 입니다.')
    else:
        if input_num == "종료":
            print('프로그램을 종료 합니다.')
            break
        else:
            print('양수만 입력 하세요')






