def solve(arr, n):
    cnt = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(n):
        for j in range(n):
            while 0<=i<n and 0<=j<n:
                K = arr[i][j]
                for c in range(4):
                    i += dr[c]
                    j += dc[c]
                    if K > arr[i][j]:
                        K = arr[i][j]
                    cnt+=1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    result = solve(Arr, N)
    print(f'#{tc} {result}')