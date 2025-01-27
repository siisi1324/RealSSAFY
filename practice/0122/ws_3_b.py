pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject, day, title=None):
    global pro_num
    data = {}
    data = {'subject':subject, 'day':day, 'title':title}
    pro_num+=1
    data['문제 번호'] = pro_num 
    return data

result_1 = create_data('python', 3)
result_2 = create_data(day=1, subject='web', title='web연습하기기')
result_3 = create_data(**global_data)

print(result_1)
print(result_2)
print(result_3)
