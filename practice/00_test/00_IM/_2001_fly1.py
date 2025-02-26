# N*N 짜리 배열 안에 한번에 최대한 많이 죽일 수 있는 숫자의 파리를 세어라

def solve(arr, n, m):
    total_sum = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]


    while True:
        num_sum = 0
        d = 0 
        i = 0
        j = 0
        for round in range(m):
            i += dr[d]
            j += dc[d]
            if 0<=i<=n and 0<=j<=n:
                num_sum += arr[i][j]
                
                





T = int(input())
N, M = map(int, input().split())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = solve(arr, M)
    print(f'#{tc} {result}')
