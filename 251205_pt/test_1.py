import pandas as pd

data = [10, 20, 30, 40]
series = pd.Series(data, index=['a', 'b', 'c', 'd'])
# print(series)
# print(type(series))

data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
series = pd.Series(data)
# print(series)

list_data = ['2024-12-01', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data, name='시리즈')
# print(sr)

idx = sr.index
# print(idx)

val = sr.values
# print(val)

# print(sr.shape)

# test 1.
kevin_score = [95, 80, 100, 85]
kevin_series = pd.Series(kevin_score, name='Kevin', index=['국어', '수학', '영어', '국사'])
# print(kevin_series)

kevin_score2 = {'국어': 95, '수학': 80, '영어': 100, '국사': 85}
kevin_series2 = pd.Series(kevin_score2, name='Kevin')
# print(kevin_series2)

# test 2.
dinner = ['4 cups', '1 cup', '2 large', '1 can']
dinner_series = pd.Series(dinner, name='Dinner', index=['밀가루', '우유', '계란', '참치캔'])

# print(dinner_series)

tuple_data = ('민지', '여', False)
member = pd.Series(tuple_data, index=['이름', '성별', '결혼여부'])

# print(member)
# print("이름: ", member['이름'])
# print("데이터\n", member[['성별', '결혼여부']])

# test 4.
# print(kevin_series)
kevin_series['수학'] = 90
# print(kevin_series)
# print(kevin_series[['국어', '영어']])
print(kevin_series[kevin_series >= 90])