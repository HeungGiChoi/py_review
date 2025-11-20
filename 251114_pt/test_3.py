# 실습
## 주어진 부모클래스를 바탕으로 조건에 만족하는 자식 클래스 설계

## 부모 클래스
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f'{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}')

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f'상품명: {self.name}')
        print(f'가격: {self.price}원')
        print(f'재고: {self.quantity}개')

class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period=12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    def extend_warranty(self, months):
        self.warranty_period += months
        print(f'보증 기간이 {months}개월 연장되었습니다. 현재 보증 기간 : {self.warranty_period}개월')

    def display_info(self):
        super().display_info()    
        print(f'보증 기간 : {self.warranty_period}개월')

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
    
    def is_expired(self, current_date):
        if self.expiration_date >= current_date:
            print(f'{self.name}는 유통기한이 지나지 않았습니다.')
        else:
            print(f'{self.name}는 유통기한이 지났습니다.')

    def display_info(self):
        super().display_info()
        print(f'유통 기한 : {self.expiration_date}')

electronic = Electronic("스마트 TV", 1500000, 5, 24)
electronic.display_info()
electronic.extend_warranty(12)
electronic.display_info()

food = Food("사과", 3000, 50, "2025-10-30")
food.display_info()
food.is_expired("2025-09-30")