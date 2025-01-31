data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}

print(data.items())
print(data.values())
if 'without' in data.keys():
    print(data['without'])
else:
    print('unknown')

for item in plus_data.keys():
    data[item] = plus_data[item]

print(data)
    