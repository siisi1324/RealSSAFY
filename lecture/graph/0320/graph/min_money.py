from heapq import heappush, heappop


def solve():
    # 다익스트라 작성
    # 시작정점에 다른 정점까지 가는데 필요한 비용을 계산
    # 특정 정점까지 비용이 확정난 정점을 재 계산 방지 및 비용 저장
    visited = [[-1] * N for _ in range(N)]
    weights = []
    heappush(weights, (0, (0, 0)))
    # 목적지 까지 비용이 확정 날 때까지 반복하면서 비용계산하기
    while True:
        # 시작점에서 비용을 최소로 들여 갈 수 있는 정점 구하기
        w, position = heappop(weights)
        # 비용이 아직 확정이 안 난 경우에만
        if visited[position[0]][position[1]] == -1:
            visited[position[0]][position[1]] = w
        else:  # 방금 가져온 비용은 비용이 이미 확정난 정점까지 가는 비용이다...
            continue  # 아무것도 하지마..
        if position == (N - 1, N - 1):
            return w
        # 방금 확정된 정점을 거쳐서 다른 정점으로 가는 비용을 계산
        # position과 인접한 정점 까지 가는 비용을 계산
        cr = position[0]
        cc = position[1]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:  # 유효한 정점이면..
                # 비용계산 : 1 + 높이차이(단, 목적지가 더 높을 때)
                new_cost = 1 + data[nr][nc] - data[cr][cc] if data[nr][nc] > data[cr][cc] else 1
                heappush(weights, (new_cost + visited[cr][cc], (nr, nc)))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 0,0에 시작해서 N-1,N-1로 가는 최소비용 계산
    # dijkstra
    result = solve()
    print(f'#{tc} {result}')