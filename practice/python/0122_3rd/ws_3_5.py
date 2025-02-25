number_of_people = 0
number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    number_of_people = number_of_people + 1


def create_user(name,age,address):
    print(f'{name}님 환영합니다!')
    user_info = {
        '이름' : name,
        '나이' : age,
        '주소' : address,
    }
    increase_user()
    return user_info

def rental_book(info):
    available_num = info['age'] // 10
    decrease_book(available_num)
    print(f'{info["name"]}님이 {available_num}권의 책을 대여 하였습니다.')


def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print(f'남은 책의 수: {number_of_book}')

many_user = list(map(create_user,name,age,address))
list(map(rental_book,list(map(lambda x : {'name':x['이름'], 'age' :x['나이']},many_user))))