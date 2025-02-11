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

# 여기서 print (create_user)를 하면 create_user의 리턴값이 없기 때문에 none이 출력이 된다. 
# 그래서 명시적으로 return '' 을 하던지 print를 없애고 함수만 호출하던지 하면 된다. 