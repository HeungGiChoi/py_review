from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

    def payment_summary(self, amount):
        print(f'{amount} 원 결제가 완료되었습니다.')

class CreditCard(PaymentSystem):
    def authenticate(self):
        print("신용카드 인증 완료.")

    def process_payment(self, amount):
        print(f'신용카드로 {amount} 원을 결제합니다.')

print("신용카드 결제: ")
credit_card = CreditCard()
credit_card.authenticate()
credit_card.process_payment(50000)
credit_card.payment_summary(50000)