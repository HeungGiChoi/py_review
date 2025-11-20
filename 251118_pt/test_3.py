## 클래스 종합 프로그래밍
# 날짜별 전력사용량
from abc import ABC, abstractmethod
import copy

electricity_usage = [
    {'date': '2024-11-01', 'usage': 12.5},
    {'date': '2024-11-02', 'usage': 15.3},
    {'date': '2024-11-03', 'usage': 10.8},
    {'date': '2024-11-04', 'usage': 14.2},
    {'date': '2024-11-05', 'usage': 13.6}
]

class ElectricityData(ABC):
    def __init__(self, usage_data, total_usage):
        ## 여기 usage_data는 electricity_usage를 대입
        ## 이 경우 copy한게 아니기 때문에 C언어의 포인터와 유사함.
        ## electricity_usage(전역변수)의 값을 변경하면 self._usage_data는 그 메모리 주소를 참조하기 때문에
        ## 똑같이 값이 변경됨. 
        self._usage_data = usage_data
        self._total_usage = total_usage

    # usage_data getter
    @property
    def usage_data(self):
        return self._usage_data
    
    # usage_data setter
    ## setter는 값을 추가하는 용도 x
    ## 완전히 새 값으로 교체하는 용도임
    @usage_data.setter
    def usage_data(self, new_data):
        self._usage_data = new_data

    # total_usage getter
    @property
    def total_usage(self):
        return self._total_usage
    
    # total_usage setter
    @total_usage.setter
    def total_usage(self, usage):
        self._total_usage = usage

    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, new_date, new_usage):
        new_data = dict(date=new_date, usage=new_usage)
        self._usage_data.append(new_data)

    ## 더 간단하게 수정 가능
    def remove_usage(self, date):
        self._usage_data[:] = [i for i in self._usage_data if i['date'] != date]
        # remove_data = [i for i in self._usage_data if i['date'] == date]
        # self._usage_data.remove(remove_data[0])

class HomeElectricityData(ElectricityData):
    def __init__(self, usage_data):
        super().__init__(usage_data, total_usage=0)
        self.total_usage = self.calculate_total_usage()
    
    def calculate_total_usage(self):
        total_usage = 0
        for i in self.usage_data:
            total_usage += i['usage']
        return round(total_usage, 1)

    def get_usage_on_date(self, date):
        day_usage = [i['usage'] for i in self._usage_data if i['date'] == date]
        print(f'{date}의 사용량: {day_usage[0]}') 
    
    ## 별도의 클래스 클래스 변수값을 넣어서 사용 가능
    @classmethod
    def filter_data(cls, data_list, str_day, end_day):
        filtering = [i for i in data_list if str_day <= i['date'] <= end_day]
        print(f'특정 날짜 범위 내 사용량: {filtering}')

    ## staticmethod(정적 메서드)를 클래스에서 사용하려면 매개변수로 값을 넘겨줘야 함.
    ## max()함수의 재발견. max의 key 매개변수. max(x, key= )
    @staticmethod
    def high_data(usage_data):
        max_item = max(usage_data, key=lambda x: x['usage'])
        print(f'가장 높은 사용량: {max_item}')

copydata = copy.deepcopy(electricity_usage)

home_data = HomeElectricityData(copydata)
print(f'총 전력 사용량: {home_data.total_usage}')
print(f'총 데이터: {home_data.usage_data}')

home_data.add_usage("2025-11-09", 4.5)
print(f'이건 usage_data: {home_data.usage_data}')
print(f'이건 electricity의 data: {electricity_usage}')

home_data.add_usage("2025-11-10", 4.5)
home_data.add_usage("2025-11-11", 4.5)
home_data.add_usage("2025-11-12", 4.5)

home_data.total_usage = home_data.calculate_total_usage()
print(home_data.total_usage)

# home_data.get_usage_on_date("2025-11-19")
# # home_data.filter_data("2024-11-03", "2024-11-05")

# home_data.high_data(electricity_usage)

home_data.remove_usage("2025-11-10")
print(home_data._usage_data)
