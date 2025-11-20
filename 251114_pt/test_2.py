class Parent:
    def greet(self):
        print('안녕하세요, 저는 부모 클래스입니다.')

class Child(Parent):
    def greet(self):
        # super().greet()
        print('안녕하세요, 저는 자식 클래스 입니다.')

parent = Parent()
child = Child()

parent.greet()
print()
child.greet()