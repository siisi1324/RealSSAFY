# N개의 상자가 모두 0으로 표기되어있는데 Q회를 돌리면서 L부터 R까지 I로 바꿔주는 작업을 수행하시오..


def solve(arr, l, r, num):
    for i in range(l, r+1):
        arr[i] = num
    return arr
    


T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for tc2 in range(Q):
        L, R = map(int, input().split())
        result = solve(arr, L-1, R-1, tc2+1)
    print(f'#{tc}', *arr)


print('====================================================')


# def solve(arr, l, r, num):
#     for i in range(l, r+1):
#         arr[i] = num  # 특정 숫자로 변경
#     return arr

# T = int(input())
# for tc in range(1, T+1):
#     N, Q = map(int, input().split())  # N: 상자 개수, Q: 작업 횟수
#     arr = [0] * N  # 상자 초기화

#     for i in range(Q):
#         L, R = map(int, input().split())  # 범위 입력
#         arr = solve(arr, L-1, R-1, i+1)  # L, R이 1부터 시작하므로 0부터 시작하도록 변환

#     print(f'#{tc}', *arr)  # 결과 출력