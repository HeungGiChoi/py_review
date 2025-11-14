# 실습 3.
## 건강상태 클래스 생성
## 운동을 하면 체력 1 증가
## 술을 마시면 체력 1 감소
## 건강 상태 : hp로 설정
## hp 범위 : 1 ~ 100

class Health:
    
    def __init__(self, name):
        self.name = name
        self._drink = 0
        self._workout = 0
        self._hp = 0

    def setdrink(self, drink):
        self._drink = drink

    def setworkout(self, workout):
        self._workout = workout

    def sethp(self, hp):
        self._hp = hp


    def getdrink(self):
        return self._drink
    
    def getworkout(self):
        return self._workout
    
    def gethp(self):
        self._hp += self._workout
        self._hp -= self._drink
        if self._hp > 100:
            self._hp = 100
        elif self._hp < 1:
            self._hp = 1
        return self._hp

p1 = Health("나몸짱")
p2 = Health("나약해")

p1.sethp(90)
p1.setworkout(5)
p1.setdrink(2)

print(f'{p1.getworkout()}시간 운동하다')
print(f'술을 {p1.getdrink()}잔 마시다')
print(f'{p1.name} - hp: {p1.gethp()}')

p2.sethp(10)
p2.setworkout(1)
p2.setdrink(12)
print(f'{p2.getworkout()}시간 운동하다')
print(f'술을 {p2.getdrink()}잔 마시다')
print(f'{p2.name} - hp: {p2.gethp()}')

print(p1.name)
print(p1._drink)
print(p1._workout)

p1._workout = 8
print(p1._workout)

## 캡슐화나 정보은닉은 개발자들이 개념을 구현하기 위하여
## 일반적인 메서드나 함수를 활용한 것일뿐
## 예약된 기능이 아니다.
## 개발자들의 관례를 통해 구현되는 '디자인 원칙' 이다.