# 붕어빵을 팔 사람들 자격을 본다
# n명의 사람만 자격을 얻었다. 
# M초에 k개 붕어빵 만들수있다. 
# N = 사람명수
# M = 초가 걸려야
# K = 개의 붕어빵을 만들 수 있다.
# 가능하면 Possible, 불가능하면 Impossible 출력

def is_fish(arr, n, p):
    for i in 


T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    p = list[map(int, input().split())]
    list1 = [0]*100
    for i in range(0, 100, m+1):
        list1[m+1] = k
    result = is_fish(list1, n, p)
    print(f'#{tc} {result}')

