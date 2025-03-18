
def no_negative(num):
    if num<0:
        return -num
    else:
        return num


negative = -3
print(no_negative(negative))



empty_list = []
print(bool(empty_list))



my_list = [1, 2, 3, 4, 5]
print(sum(my_list))

unsorted_list = ['하', '교', '캅', '의', '지', '가']
listlist = sorted(unsorted_list)
print(listlist)