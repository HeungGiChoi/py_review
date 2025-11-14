class Test:

    def __init__(self, name):
        self.name = name

    def returns(self):
        return f'이것은 returns {self.name}'

test1 = Test('최흥기')
print(test1)