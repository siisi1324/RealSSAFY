name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 책의 수를 초기화
number_of_book = 100

# 사용자 정보를 생성하는 함수
def create_user(name, age, address):
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다.')
    return user_info

# 책의 수를 감소시키는 함수
def decrease_book(borrow):
    global number_of_book
    number_of_book -= borrow
    return number_of_book

# 책을 대여하는 함수
def rental_book(user, borrow_count):
    remaining_books = decrease_book(borrow_count)
    print(f'{user["name"]}님이 {borrow_count}권의 책을 대여하였습니다.')
    print(f'남은 책의 수 : {remaining_books}')

# 사용자 리스트 생성
many_user = list(map(create_user, name, age, address))

# 각 사용자가 책을 대여하는 프로세스
for user in many_user:
    borrow_count = user['age'] // 10  # 나이를 기준으로 빌리는 책 수 계산
    rental_book(user, borrow_count)