# 전역 변수
number_of_book = 100

# 사용자 정보를 생성하는 함수
def create_user(name, age, address):
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다.')
    return user_info

# 책 대여 처리 함수
def rental_book(user):
    global number_of_book
    borrow_count = user['age'] // 10  # 나이를 기준으로 빌리는 책 수 계산
    number_of_book -= borrow_count
    print(f'남은 책의 수: {number_of_book}')
    print(f'{user["name"]}님이 {borrow_count}권의 책을 대여하였습니다.')

# 데이터 초기화
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 사용자 생성
many_user = list(map(create_user, name, age, address))

# 각 사용자가 책을 대여하는 프로세스
for user in many_user:
    rental_book(user)

