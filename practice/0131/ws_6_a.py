my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

for tem in my_set:
    if tem in my_dict.keys():
        print(my_dict.get(tem))
    else:
        print('None')

var = (1, 2, 3)
my_dict[var] = '변수로도 키 설정 가능'

print(my_dict)