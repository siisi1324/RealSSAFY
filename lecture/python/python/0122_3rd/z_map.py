def create_user(user_info):
    name, age, address = user_info
    print(f'{name}님 환영합니다!')
    return {'name':name, 'age':age, 'address':address}

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_info_list = zip(name, age, address)
# print(list(user_info_list))
result = list(map(create_user, user_info_list))
print(result)