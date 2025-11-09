## 과제 1. 자판기 프로그램

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

## 사용자는 '소비자', '주인' 두 가지 종류로 입력받기. 그 외 값은 잘못된 값으로 출력
## '소비자'일땐 마시고 싶은 음료 입력받기
    ## 값이 있으면 vending_machine에서 제거, 없으면 '없음' 출력
## '주인' 일 때 '추가', '삭제' 두 가지 종류 입력 받기. 그 외 값은 잘못된 값으로 출력
    ## '추가'일 때, 추가할 음료수 입력받고 vending_machine에 추가 후, 같은 값끼리 정렬되도록 출력
    ## '삭제'일 때, 삭제할 음료수 입력받고 값이 있으면 제 거, 없으면 '없음' 출력
print(f'남은 음료수: {vending_machine}')
print()
while True: 
    user_input = input('사용자 종류를 입력하세요: \n1.소비자\n2.주인\n')
    if user_input == '종료':
        print('자판기 프로그램을 종료합니다.')
        break
    elif user_input != '소비자' and user_input != '주인' and user_input != '1' and user_input != '2':
        print('잘못된 값을 입력하셨습니다. 사용자를 다시 입력해주세요.')
        continue
    elif user_input == '소비자' or user_input == '1':
        while True:
            input_drink = input('마시고 싶은 음료? ')
            if input_drink in vending_machine:
                print(f'{input_drink} 드릴께요.')
                vending_machine.remove(input_drink)
                print(f'남은 음료수: {vending_machine}')
                break
            else:
                print(f'{input_drink}는 지금 없네요.')
                continue
    elif user_input == '주인' or user_input == '2':
        while True:
            insert_del = input('할 일 선택: \n1.추가\n2.삭제\n')
            if insert_del != '추가' and insert_del != '삭제' and insert_del != '1' and insert_del != '2':
                print('잘못된 값을 입력하셨습니다. 할 일을 다시 선택해주세요.')
                continue
            if insert_del == '추가' or insert_del == '1':
                print(f'남은 음료수: {vending_machine}')
                print()
                add_drink = input('추가할 음료수? ')
                vending_machine.append(add_drink)
                vending_machine.sort()
                print('추가 완료')
                print(f'남은 음료수: {vending_machine}')
                break
            if insert_del == '삭제' or insert_del == '2':
                print(f'남은 음료수: {vending_machine}')
                del_drink = input('삭제할 음료수? ')
                if del_drink in vending_machine:
                    vending_machine.remove(del_drink)
                    print('삭제 완료')
                    print(f'남은 음료수: {vending_machine}')
                    break
                else:
                    print(f'{del_drink}는 지금 없네요.')
                    break