def my_multi(number_1, number_2):
    return number_1*number_2

def is_negative(number):
    if number<=0:
        return True
    else:
        return False

def is_negative(number):
    return number <= 0


def default_arg_func(default='기본값'):
        return default


result_1 = my_multi(2, 3)
print(result_1)
result_2 = is_negative(3)
print(result_2)
result_3 = default_arg_func()
print(result_3)
result_4 = default_arg_func('다른 값')
print(result_4)
