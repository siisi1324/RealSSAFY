# 한번 숫자를 입력하면 끝까지 숫자가 적용되는데, 몇 번 바꿔야 하는가?

def solve(list1, list2, d):
    cnt = 0 # 몇 번 바뀌는지 
    for i in list1: # 숫자들보면서
        if i == list2[d]: # 그대로면 (초기화 숫자가 0)
            pass # 패스해라~
        else: # 아니면
            d = (d+1)%2 # d인덱스를 바꿔서, 1이나 0으로 바꿔라
            cnt += 1 # 카운트도 늘리고
    return cnt # 카운트 리턴


T = int(input())
for tc in range(1, T+1):
    num_1 = list(input()) # 2진수 숫자
    num_2 = ['0', '1'] # 2진수
    d = 0 # 인덱스 조절용
    result = solve(num_1, num_2, d)
    print(f'#{tc} {result}')
