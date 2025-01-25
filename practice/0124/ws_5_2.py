# def remove_duplicates(list_origin):
#     set1 = set(list_origin)
#     new_lst = sorted(list(set1))
#     return new_lst


# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)


def remove_duplicates(list_origin):
    new_lst = []
    for i in list_origin:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)