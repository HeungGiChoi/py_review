# 실습 예제 1.
## 날씨 데이터는 2차원 리스트 형태
## 날짜, 지역, 온도, 강수량 순서 

## 아래 종류의 함수들을 제작
    ## 도시별 평균기온 계산 함수
    ## 도시별 최고/최소 기온 찾기 함수
    ## 도시별 강수량 분석 함수
    ## 데이터 추가 함수
    ## 전체 데이터 출력 함수

weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]

def avg_temp(city):
    temp_data = [i[2] for i in weather_data if i[1] == city]
    avg_temps = sum(temp_data) / len(temp_data)
    return avg_temps

def min_max_temp(city):
    temp_data = [i[2] for i in weather_data if i[1] == city]
    max_temp = max(temp_data)
    min_temp = min(temp_data)
    return [max_temp, min_temp]

def city_rain(city):
    rain_data = [i[3] for i in weather_data if i[1] == city]
    rain_day = [i for i in rain_data if i >= 0.1]
    sum_rain = sum(rain_data)
    return [rain_day, sum_rain]

def add_data(day, city, temp, rain):
    new_data = [day, city, temp, rain]
    weather_data.append(new_data)
    print(f'{city}의 날씨 데이터가 추가되었습니다.')

def print_data():
    print('현재 저장된 날씨 데이터: ')
    for i in weather_data:
        print(f'날짜: {i[0]}, 도시: {i[1]}, 평균 기온: {i[2]}℃, 강수량: {i[3]:.1f}mm')

while True:
    print('[날씨 데이터 분석 프로그램]')
    print('1. 평균 기온 계산')
    print('2. 최고/최저 기온 찾기')
    print('3. 강수량 분석')
    print('4. 날씨 데이터 추가')
    print('5. 전체 데이터 출력')
    print('6. 종료')
    func_input = input('원하는 기능의 번호를 입력하세요: ')
    
    if func_input != '1' and func_input != '2' and func_input != '3' and func_input != '4' and func_input != '5' and func_input != '6':
        print('잘못 입력하셨습니다. 1 ~ 6번 중 하나를 선택해주세요.')
        continue 
    elif func_input == '1':
        city_input = input('도시 이름을 입력하세요: ')
        average_temp = avg_temp(city_input)
        print(f'{city_input}의 평균 기온: {average_temp:.2f}℃')
        print()
        continue
    elif func_input == '2':
        city_input = input('도시 이름을 입력하세요: ')
        min_max_data = min_max_temp(city_input)
        print(f'{city_input}의 최고 기온: {min_max_data[0]:.1f}℃, 최저 기온: {min_max_data[1]:.1f}℃')
        print()
        continue
    elif func_input == '3':
        city_input = input('도시 이름을 입력하세요: ')
        rain_data = city_rain(city_input)
        print(f'{city_input}의 총 강수량: {rain_data[1]}mm')
        print(f'{city_input}의 강수량이 있었던 날: {len(rain_data[0])}일')
        print()
        continue
    elif func_input == '4':
        day_input = input('날짜를 입력하세요 (YYYY-MM-DD): ')
        city_input = input('도시를 입력하세요: ')
        temp_input = float(input('평균 기온을 입력하세요: '))
        rain_input = float(input('강수량을 입력하세요 (mm): '))
        add_data(day_input, city_input, temp_input, rain_input)
        print()
        continue
    elif func_input == '5':
        print_data()
        print()
        continue
    elif func_input == '6':
        print('프로그램을 종료합니다. ')
        break
