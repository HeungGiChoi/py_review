class Calculation:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print(f'{self.num1 + self.num2}')
    
    def sub(self):
        print(f'{self.num1 - self.num2}')
    
    def mul(self):
        print(f'{self.num1 * self.num2}')
    
    def div(self):
        print(f'{self.num1 / self.num2}')
    
calc = Calculation(3, 5)

calc.div()
calc.sub()