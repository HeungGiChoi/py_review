# 클래스 복습
## 부모 클래스
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount
        print(f'{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다.')

    def display_info(self):
        print(f'상품명: {self.name}')
        print(f'가격: {self.price}')
        print(f'재고: {self.quantity}')
    
class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period=12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period
    
    def extend_warranty(self, months):
        self.warranty_period += months
        print(f'보증 기간이 {months}개월 연장되었습니다. 현재 보증 기간: {self.warranty_period}개월')
    
    def display_info(self):
        super().display_info()
        print(f'보증 기간: {self.warranty_period}개월')