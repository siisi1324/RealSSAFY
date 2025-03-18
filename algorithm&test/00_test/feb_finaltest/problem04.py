# 1번 중복제거
# 2번 양수와 음수의 합 각각
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    list_2 = []
    for i in items_list:
        if i not in list_2:
            list_2.append(i)
        else:
            continue
        
    plus_num = 0
    min_num = 0
    for i in list_2:
        try:
            if int(i)>0:
                    plus_num += i
            elif int(i)<0:
                    min_num += i
        except:
            continue

    return list_2, (plus_num, min_num)

print(analyze_items([2, 2, 2, "a", "a", 3, 0, -2]))
# 예시 결과: ([2, "a", 3, 0, -2], (5, -2))

print(analyze_items([]))
# 예시 결과: ([], (0, 0))

print(analyze_items(["apple", "apple", "banana"]))
# 예시 결과: (["apple", "banana"], (0, 0))
