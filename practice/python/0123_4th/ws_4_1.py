import requests
from pprint import pprint as print
# from pprint import pprint 라고 import하면 바로 pprint로 써도 예쁘게 출력을 시켜주고,
# import pprint만 하면 pprint.pprint(무언가) 이런식으로 출력해야하고,
# from pprint import pprint as print 이렇게 하면 print를 쓰는 것만으로도 pprint.pprint(무언가)를 쓰는 효과가 난다. 

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
print(response)

# # 변환 데이터 출력
print(parsed_data)
# # 변환 데이터의 타입dla
print(type(parsed_data))

# # 특정 데이터 출력
print(parsed_data['name'])
print(parsed_data['username'])
print(parsed_data['company']['name'])