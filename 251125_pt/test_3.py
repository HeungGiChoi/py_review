# 예외처리
# try:
#     # 예외가 발생할 가능성이 있는 코드
#     x = int(input('숫자를 입력하세요: '))
#     result = 10 / x
# except ZeroDivisionError: # 특정 예외 처리
#     print('0으로 나눌 수 없습니다.')
# except ValueError:
#     print('유효한 숫자가 아닙니다.')
# else:
#     #예외가 발생하지 않았을때 실행
#     print('결과: ', result)
# finally:
#     # 예외 발생 여부와 상관없이 항상 실행
#     print('프로그램이 종료됩니다.')

# try:
#     x = int('abc')
# except ValueError as e:
#     print('예외 메시지: ', e)

# try:
#     x = int(input('숫자를 입력하세요:'))
#     result = 10 / x
# except (ValueError, ZeroDivisionError) as e:
#     print('예외 발생: ', e)

def div(a, b):
    if b == 0:
        raise ZeroDivisionError('0으로 나눌 수 없습니다.')
    return a / b

try:
    result = div(10, 0)
except ZeroDivisionError as e:
    print('예외 발생:', e)
