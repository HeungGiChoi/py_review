dict_1 = {
    "name": "최흥기",
    "age": 32,
    "city": "서울"
}

print(dict_1)

dict_2 = dict(name="임유연", age=27, city="서울")
print(dict_2)

dict_2['hobby'] = "헬스"
print(dict_2)
dict_2['name'] = "최흥기"
print(dict_2)

del dict_2['name']
print(dict_2)

print(dict_1.values())
print(dict_1.keys())

print(dict_1.items())
list_1 = dict_1.items()
print(list_1)