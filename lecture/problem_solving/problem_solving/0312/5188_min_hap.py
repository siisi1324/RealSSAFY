def find_min_path(r, c, total_cost):
    if r >= N or c >= N:  # 범위를 벗어나면 큰 값 반환
        return float('inf')

    total_cost += grid[r][c]

    if r == N - 1 and c == N - 1:  # 목적지 도착
        return total_cost

    # 오른쪽, 아래쪽 이동 중 최소 비용 선택
    return min(find_min_path(r, c + 1, total_cost), find_min_path(r + 1, c, total_cost))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_cost = find_min_path(0, 0, 0)
    print(f'#{tc} {min_cost}')
