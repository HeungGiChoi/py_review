# from datetime import datetime, timedelta

# now = datetime.today()
# print(now)
# print(now.year)
# print(now.hour)

# print(f'{now.year}년 {now.month}월 {now.day}일')
# print(f'{now.hour}시 {now.minute}분 {now.second}초')

# now = datetime.now()
# print("현재 날짜와 시간 : ", 
# 
# now)

from datetime import date

print(" 지금까지 몇 일?")

first_day = date(year=2024, month=11, day=18)
print(first_day)

today = date.today()
print(today)
print(date.today().weekday())

pass_time = today - first_day
print(pass_time)

print(f'과거로부터 {pass_time.days} 지났다.')