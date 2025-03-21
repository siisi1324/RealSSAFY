T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    num = 1

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    i, j = 0, 0

    while num <= N * N:
        arr[i][j] = num
        num += 1

        new_i = i + dr[d]
        new_j = j + dc[d]

        # 배열 범위를 벗어나거나 이미 값이 채워져 있다면 방향 변경
        if not (0 <= new_i < N and 0 <= new_j < N and arr[new_i][new_j] == 0):
            d = (d + 1) % 4  # 방향 변경
            new_i = i + dr[d]
            new_j = j + dc[d]

        i, j = new_i, new_j  # 새 위치로 이동


    print(f'#{tc}')
    for row in arr:
        print(*row)

