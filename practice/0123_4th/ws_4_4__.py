user_list = [
    {'name': 'Ervin Howell', 
        'company': 'Deckow-Crist', 'lat': -43.9509, 'lng': -34.4618}, 
    {'name': 'Clementine Bauch', 
        'company': 'Romaguera-Jacobson', 'lat': -68.6102, 'lng': -47.0653}, 
    {'name': 'Chelsey Dietrich', 
        'company': 'Keebler LLC', 'lat': -31.8129, 'lng': 62.5342}, 
    {'name': 'Mrs. Dennis Schulist', 
        'company': 'Considine-Lockman', 'lat': -71.4197, 'lng': 71.7478}, 
    {'name': 'Kurtis Weissnat', 
        'company': 'Johns Group', 'lat': 24.8918, 'lng': 21.8984}, 
    {'name': 'Clementina DuBuque', 
        'company': 'Hoeger LLC', 'lat': -38.2386, 'lng': 57.2232}]


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        if censorship(user):
        #     if user['company'] in censored_user_list.keys():
        #         censored_user_list[user['company']].append(user['name'])
        #         # 이미 회사 키가 존재할 경우 값을 추가하는 것으로 append사용
        #     else:
                
                # censored_user_list[user['company']] = [user['name']]
        # setDefault() : 기존 키 값이 있으면 기존 값 반환, 없으면 default값을 반환
            emp_list = censored_user_list.setdefault(user['company'],[])
            emp_list.append(user['name'])
            # 여기서 emp_list가 이미 리스트 형식으로 반환이 되어있어서 append하면 된다. 

    return censored_user_list


def censorship(someone):
    if someone['company'] in black_list:
        print(f"{someone['company']} 소속의 {someone['name']}은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상 없습니다.')
        return True
        

dap = create_user(user_list)
from pprint import pprint  # 보기 좋게 출력
pprint(dap)
