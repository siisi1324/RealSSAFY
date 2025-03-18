def union_sets(set1, set2):
    return set1.union(set2)

def union_multiple_sets(*sets):
    if len(sets) < 2:
        return "최소 두 개의 셋이 필요합니다"
    result_set = set()
    for s in sets:
        result_set = result_set.union(s)
    return result_set


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  

result = union_multiple_sets({1, 2})
print(result)
