# 첫 줄에 트리의 정점 총 V가 있고, 그 다음줄부터 V-1개의 간선이 나열된다. 항상 부모 - 자식 순으로 표기되는데, 이것을 전위 순회하여 정점의 번호를 출력하시오.

def pre_order(num):
    if num:
        pre_order(arr_l[num])
        print(num)
        pre_order(arr_r[num])


V = int(input())
E = V - 1

arr_l = [0]*(V+1)
arr_r = [0]*(V+1)
lst = list(map(int, input().split()))
print(lst)
for i in range(E):
    p, c = lst[i*2], lst[i*2+1]
    if arr_l[p] == 0:
        arr_l[p] = c
    else:
        arr_r[p] = c

pre_order(1)
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13