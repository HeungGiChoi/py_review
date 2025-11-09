## 자판기 프로그램 함수화

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

# 남은 음료수 확인
def check_machine():
    print(f'남은 음료수: {vending_machine}')
    print()

# 자판기에 음료수가 있는지 확인
def is_drink(drink):
    if drink in vending_machine:
        return True
    else:
        return False

# 음료수를 추가
def add_drink(drink):
    vending_machine.append(drink)
    vending_machine.sort()

# 음료수 삭제
def remove_drink(drink):
    vending_machine.remove(drink)
    
check_machine()

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
            if is_drink(input_drink):
                print(f'{input_drink} 드릴께요.')
                remove_drink(input_drink)
                check_machine()
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
                check_machine()
                drink_add = input('추가할 음료수? ')
                add_drink(drink_add)
                print('추가 완료')
                check_machine()
                break
            if insert_del == '삭제' or insert_del == '2':
                check_machine()
                del_drink = input('삭제할 음료수? ')
                if is_drink(del_drink):
                    remove_drink(del_drink)
                    print('삭제 완료')
                    check_machine()
                    break
                else:
                    print(f'{del_drink}는 지금 없네요.')
                    break
