# 전역변수
# quantity = 2

# def get_price():
#     price = 4000 * quantity
#     return price

# unit_price = get_price()
# print(f'{quantity}개에 {unit_price}원 입니다.')

# a = 11

# def calculate_sum():
#     # a = 7
#     total = 0
#     for i in range(1, a):
#         total += i
#     return total

# print(calculate_sum())
# print(a)

# x = 0

# def oneUp():
#     global x
#     x = x + 1
#     return x

# print(oneUp())
# print(oneUp())
# print(x)

# def introduce(name, age, city):
#     print(f'이름: {name}')
#     print(f'나이: {age}')
#     print(f'사는곳: {city}')

# introduce(city="서울", name="홍길동", age=12)
# introduce("홍길동", city="서울", age=12)

# def calc_avg(*args):
#     sums = 0
#     for i in args:
#         sums += i
#     average = sums / len(args)
#     return average

# print(calc_avg(1, 2))
# print(calc_avg(1, 2, 3, 4, 5))

# def text_def(a, *args):
#     print("a: ", a)
#     print("args: ", args)

# text_def(1, 2, 3, 4, 5)

def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

introduce(name="최흥기", age=32, city="서울")

