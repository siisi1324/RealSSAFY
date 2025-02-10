def snail(n, arr):
    r, c = 0, 0
    num = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    while True:
        if num == n*n+1:
            break
        arr[r][c] = num
        r += dr[d]
        c += dc[d]
        num += 1
        if r>=n or r<0 or c>=n or c<0 or arr[r][c]:
            r-=dr[d]
            c-=dc[d]
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    return arr


T = int(input())

for tc in range (1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    result = snail(n, arr)
    print(f'#{tc}', end=' ')
    print()
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
