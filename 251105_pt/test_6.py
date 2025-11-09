## format() 활용 포맷팅
# country = "대한민국"
# people = "한국인"
# city = "서울"

# text = "저는 올해 {0}살 입니다.".format(20)
# print(text)
# text = "저는 {0}사람이며 {1}에 살고 있습니다.".format(country, city)
# print(text)
# text = "제가 사는 {0}은 {country}에 있습니다.".format(city, country="한국")
# print(text)
# text = "나는 {1} 이다. {{그리고}} {0}에 산다.".format(city, people)
# print(text)
# text = "{}점수: {}점, {}점수: {}점".format("영어", 100, "수학", 95)
# print(text)

## f문자열 포맷팅
name = "홍길동"
age = 20
text = f'내 이름은 {name} 입니다. 나이는 {age + 1} 살 입니다.'
print(text)

text = f'내 이름은 [{name:!^20}]'
print(text)
