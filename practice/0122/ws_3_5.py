name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    many_user = dict()
    many_user['name'] = name
    many_user['age'] = age
    many_user['address'] = address
    print(f'{name}님 환영합니다.')
    return many_user

number_of_book = 100

def decrease_book():
    global number_of_book
    last_book = number_of_book - (many_user[1])//10
    print(f'{many_user[0]}님이 {(many_user[1])//10}권의 책을 대여하였습니다.')
    print(f'남은 책의 수 : {last_book}')

many_user = list(map, decrease_book(many_user))
print(many_user)


# def rental_book(info):
#     pass


def rental_book(name, number):
    boooks = decrease_book(number)
    print(f'남은 책의 수 : {boooks}')
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')


number_of_book = 100

def decrease_book(borrow):
    global number_of_book
    last_book = number_of_book - borrow
    return last_book
