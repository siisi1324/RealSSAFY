number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people


def create_user(name, age, address):
    print(f'현재 가입 된 유저 수 : {number_of_people}')
    print(f'{name}님 환영합니다!')
    user_info={'name':name, 'age':age, 'address':address}
    print(user_info)
    print(f'현재 가입 된 유저 수 : {increase_user()}')

print(create_user('홍길동', 30, '서울'))