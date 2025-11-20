from abc import ABC, abstractmethod

data1 = [
    {"date": "2025-11-01", "usage": 12.5},
    {"date": "2025-11-02", "usage": 11.5},
    {"date": "2025-11-03", "usage": 13.5}
]

# print(data1)
# def add1(new_date, new_usage):
#     new_data = dict(date=new_date, usage=new_usage)
#     # print(new_data)
#     data1.append(new_data)

# add1("2025-11-04", 18.2)
# print(data1)
# def del_data():
#     total_value = 0
#     for i in data1:
#         total_value += i['usage']
#     return total_value
#         # print(i['usage'])
#         # if i['date'] == date:
#         #     data1.remove(i)

# a = del_data()
# print(a)
class A(ABC):
    def __init__(self, a, b):
        self._a = a
        self._b = b
    
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value1):
        self._a = value1

    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, value):
        self._b = value

    @abstractmethod
    def anything(self):
        pass

class Son(A):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def anything(self):
        return self._a + self._b
    
son = Son(2, 3)
print(son.a)
print(son.b)

# son.a = 4
# son.b = 8
# print(son.a)
# print(son.b)

# son.a = 4, 8
# print(son.a)

# filtering = [i for i in data1 if i['date'] >= "2025-11-01" and i['date'] <= "2025-11-03"]
# print(filtering)

electricity_usage = [
    {'date': '2024-11-01', 'usage': 12.5},
    {'date': '2024-11-02', 'usage': 15.3},
    {'date': '2024-11-03', 'usage': 10.8},
    {'date': '2024-11-04', 'usage': 14.2},
    {'date': '2024-11-05', 'usage': 13.6}
]

filtering = max(electricity_usage, key=lambda x: x['usage'])
print(filtering)

    