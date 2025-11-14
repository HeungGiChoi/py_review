# 클래스 예제 1.

## Supermarket 클래스
## 클래스 선언 시, location / name / product / customer 인자로 받기
## location : 위치 / name : 가게 이름 / product : 파는 물건 / customer : 고객의 수
## print_location() : 위치 출력 함수
## change_category() : 받은 인자로 파는 물건 바꾸는 함수
## show_list() : 현재 파는 물건 출력
## enter_customer() : 손님 수 1씩 늘리는 함수
## show_info() : 가게 이름, 위치, 파는 물건, 손님 수 모두 출력

class Supermarket:

    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
    
    def print_location(self):
        print(f'위치: {self.location}')
    
    def change_category(self, product):
        self.product = product
        print(f'{product}로 판매상품 변경.')

    def show_list(self):
        print(f'상품: {self.product}')

    def enter_customer(self):
        self.customer += 1
    
    def show_info(self):
        print(f'위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}')

supermarket1 = Supermarket("구로구 궁동", "궁동 해피마트", "라면", 10)
supermarket2 = Supermarket("구로구 개봉동", "개봉동 Y마트", "과일", 20)

supermarket1.show_info()
supermarket1.enter_customer()
supermarket1.enter_customer()
supermarket1.enter_customer()
supermarket1.enter_customer()
supermarket1.show_info()

supermarket1.show_list()
supermarket1.change_category("고기")
supermarket1.show_list()
supermarket1.print_location()