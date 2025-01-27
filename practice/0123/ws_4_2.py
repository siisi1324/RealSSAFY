import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
# API 요청

dummy_data = []
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # 마지막 숫자({i})는 요청하려는 특정 유저의 고유 ID(번호)를 의미, 0은 존재하지 못한다.
    # {i}는 f-string 안에서 삽입이 가능해서 f를 적어줘야 한다. 
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])

print(dummy_data)