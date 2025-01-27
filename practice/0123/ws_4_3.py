import requests
from pprint import pprint as print


dummy_data = []
for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()


     # lat, lng 값을 float으로 변환
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    
    # 조건에 맞는 경우만 데이터를 추가
    if -80 < lat < 80 and -80 < lng < 80:
        dum_data = {
        'name':parsed_data['name'],
        'lat':parsed_data['address']['geo']['lat'],
        'lng':parsed_data['address']['geo']['lng'],
        'company name':parsed_data['company']['name']}
        dummy_data.append(dum_data)

print(dummy_data)

    
    