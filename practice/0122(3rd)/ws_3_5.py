number_of_people = 0
number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people
    

def decrease_book(info):
    global number_of_book
    number_of_book -= info['age']//10
    return number_of_book

def create_user(name, age, address):
    user_dict = {'name' : name, 'age' : age, 'address' : address}
    return user_dict


def rental_book(info):
    

many_user = list(map(create_user, name, age, address))
info = list(map(rental_book, name, age))

print(many_user)

