# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 번갈아 정렬하는 방법
# 10 1 9 2 8 3 7 4 7 6 5

def new_sort(arr_list, n) : 
    new_list = sorted(arr_list, reverse=True)
    list_sin = []

    for i in range(n//2+1):
        list_sin.append(new_list[i])
        if new_list[i] not in list_sin:
            list_sin.append(new_list[n-1-i])

    
    
    list_sin2 = list_sin[:10]
    return list_sin2


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    good_arr = new_sort(arr, n)
    print(f'#{tc}', end=" ")
    for i in good_arr:
        print(f'{i}', end=' ')
    print()

print('==============================================================')
# 박상훈님 코드

T = int(input())  # test case
 
for i in range(1, T + 1):  # test case 번호를 위해 1, T + 1로 진행.
 
    N = int(input())  # 숫자 갯수
 
    ai = list(map(int, input().split()))  # 숫자를 list 형태로 받음
    L = len(ai)  # 받은 숫자 list의 길이
 
    for j in range(0, L, 2):  # 숫자가 두 개씩 동시에 정렬되기 때문에 2칸을 뛰어넘으며 정렬.
        max_idx = j  # max 값의 index 를 찾기 위해 변수 설정
        min_idx = j  # min 값의 index 를 찾기 위해 변수 설정
         
        for k in range(j + 1, L):  # max_idx를 찾는다.
            if ai[max_idx] < ai[k]:
                max_idx = k
         
        ai[j], ai[max_idx] = ai[max_idx], ai[j]  # max_idx와 홀수 번째 요소를 교환.
         
        for l in range(j + 1, L):  # min_idx를 찾는다.
            if ai[min_idx] > ai[l]:
                min_idx = l
         
        if j + 1 >= L:  # list의 길이를 넘어가는 경우 위치를 바꾸지 않고 종료.
            break
        else:
            ai[j + 1], ai[min_idx] = ai[min_idx], ai[j + 1]  # min_idx와 짝수 번째 요소를 교환.
         
    print(f'#{i}', end = ' ')
    if L > 10:
        for m in range(10):
            print(ai[m], end = ' ')
    else:
        for m in range(L):
            print(ai[m], end = ' ')
    print('')



print('=====================================================')

# 김유영님 코드
def new_sort (lst):
    l = len(lst)
 
    for i in range(l-1):
        min_idx = i 
 
        for j in range(i+1,l): #i 다음 요소 가져와야해서.
            if lst[min_idx] > lst[j]: #기존 최소값과 요소 비교
                min_idx = j
 
        lst[i],lst[min_idx] = lst[min_idx],lst[i]
     
 
 
t = int(input())
 
for k in range(1,t+1):
    n = int(input()) #정수의 개수
    ai = list(map(int,input().split())) #정수 리스트
 
    new_sort(ai)
     
    new_lst = []
    for a in range(5):
        new_lst.append(ai[-(a+1)])
        new_lst.append(ai[a])
 
    print(f'#{k}', *new_lst)