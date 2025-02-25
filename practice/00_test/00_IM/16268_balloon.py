# 풍선하나를 터뜨리면 상하좌우까지 총 5칸의 풍선이 날라간다.
# 최대의 꽃가루를 날릴 수 있는 경우를 말하시오.

def pop_balloon(arr, n, m):
    dr = [0, 1, 0, -1, 0]
    dc = [0, 0, 1, 0, -1]

    max_value = 0
    for i in range(n):
        for j in range(m):
            total_num = 0
            for k in range(5):
                r = i + dr[k]
                c = j + dc[k]
                if (0<=r<n) and (0<=c<m): 
                    total_num += arr[r][c]
            if max_value < total_num:
                max_value = total_num
    return max_value




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = pop_balloon(arr, N, M)
    print(f'#{tc} {result}')
