# 아래 함수를 수정하시오.
def add_item_to_dict(dict1, key, value):
    dict1[key] = value
    new_dict = dict1.copy()
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
