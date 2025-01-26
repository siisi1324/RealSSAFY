import requests

dummy_data = []
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'

    response = requests.get(API_URL)

    parsed_data = response.json()
    name = parsed_data['name']
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    company = parsed_data['company']['name']
    if -80 < lat < 80 and - 80 < lng < 80 :
        dummy_data.append({
            'name' : name
            'company' : company
            'lat' : lat
            'lng' : lng
        })

print(dummy_data)