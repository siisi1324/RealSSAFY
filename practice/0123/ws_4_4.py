user_list = [
    {'name': 'Ervin Howell', 
        'company': 'Deckow-Crist', 'lat': -43.9509, 'lng': -34.4618}, 
    {'name': 'Clementine Bauch', 
        'company': 'Deckow-Crist', 'lat': -68.6102, 'lng': -47.0653}, 
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
             censored_user_list[user['company']]=[user['name']]
        else:
             continue
    return censored_user_list


def censorship(someone):
    if someone['company'] in black_list:
            print(f"{someone['company']} 소속의 {someone['name']}은/는 등록할 수 없습니다.")
            return False
    else:
         print('이상 없습니다.')
         return True
        

dap = create_user(user_list)
print(dap)