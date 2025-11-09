while True:
    print('가나다라')
    while True:
        print('마바사')
        input_str = input('입력하세요. ')
        if input_str == '종료':
            break
    print('아자차카')

## while 내부에 있는 break는
## 한 개의 while만을 탈출한다.
## 이중 while문인 상황에서 바깥쪽 while문이 아닌
## 내부 while문에 break가 있다면
## 내부 while문 탈출하고 바깥 while문을 다시 만나게 된다.