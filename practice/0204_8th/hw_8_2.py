def check_number():
    num = input("숫자를 입력하세요 : ")
    try:
        if int(num)>0:
            print(f'양수입니다.')
        elif int(num)==0:
            print(f'0입니다.')
        elif int(num)<0:
            print(f'음수입니다.')
    except:
        print('잘못된 입력입니다.')



for i in range(4):
    check_number()
