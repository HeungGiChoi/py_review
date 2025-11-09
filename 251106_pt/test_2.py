shop = ["반팔", "청바지", "이어폰", "키보드"]

print(shop[2])
print(shop[2-1])

print(shop[-2:])

my_shop = ["반팔", "청바지", "이어폰", ["무선 키보드", "유선 키보드", "기계식 키보드"]]
print(my_shop[3])
print(my_shop[-1])
print(my_shop[2:4])
print(my_shop[3][0])

## 값 수정
shop[0] = "긴팔"
print(shop)
# shop[50] = "오빠"
# print(shop)

del shop[1]
print(shop)

del shop[0:2]
print(shop)

