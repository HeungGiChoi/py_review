# for i in range(5):
#     print(i)

# for i in range(1, 6, 2):
#     print(i)

# range의 step을 사용하려면 start와 end를 함께 작성해야 한다.
# (10, 2) <--처럼 0~10까지 2step 을 생각하고 작성하면 진행 x. 
# 컴퓨터는 10부터 2까지 어떻게? 라고 반응하며 아무것도 출력하지 않음.
# for i in range(0, 10, 3):
#     print(i)

# fruits = ['바나나', '사과', '파인애플']
# for i in fruits:
#     print(i, end=" ")

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print(total)
# numbers = [1, 3, 5, 7, 9, 11]
# for num in numbers:
#     if num > 6:
#         print(num, end=" ")

## 리스트 내포

squares = [x ** 2 for x in range(1, 11)]
print(squares)

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)

## 딕셔너리와 for문

my_dict = {'name': '홍길동', 'color': 'blue', 1: 'my love', 'hobby': 'soccer'}
for key in my_dict:
    print(key, end=" ")
print()
for value in my_dict.values():
    print(value, end=" ")
print()
for key in my_dict:
    print(f'{key}: {my_dict[key]}, ', end=" ")
print()
for key, value in my_dict.items():
    print(f'{key}: {value}, ', end=" ")

