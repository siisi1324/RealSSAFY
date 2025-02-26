# 홀수형 N*N의 농장이 있는데, 딱 맞는 마름모의 점수의 합을 구하라.

def solve(arr, n):
    cnt = 0
    r, c = 0, n//2

    while c < n:
        cnt += arr[r][c]
        r += 1
        c -= 1
        arr[r][c:c+2]




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = solve(arr, N)
    print(f'#{tc} {result}')