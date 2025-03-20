def dijkstra(S, G):
    distance = [0xfffffff] * (N + 1)  # 시작 정점에서 다른 정점까지 가는 비용
    distance[S] = 0
    checked = set()  # 비용이 확정된 정점의 모음
    # 모든 정점까지 가는 비용 계산
    while len(checked) < N + 1:
        min_v = -1
        min_distance = 0xfffffff
        # 최소비용으로 갈 수 있는 정점 선택
        for i in range(N + 1):
            if i not in checked and distance[i] < min_distance:
                min_distance = distance[i]
                min_v = i
        checked.add(min_v)
        # 선택된 정점을 거쳐서 다른 정점으로 갈 수 있는 비용 수정
        for i in range(N + 1):
            # 시작 정점에서 min_v를 거쳐서 i로 가는 비용
            # 시작정점에서 min_v로 가는비용 : distance[min_v]
            # 원래 내가 알고있던 i로 가는 비용 distance[i]
            if i not in checked and g[min_v][i] and g[min_v][i] + distance[min_v] < distance[i]:
                distance[i] = g[min_v][i] + distance[min_v]
    return distance[G]


T = int(input())
for tc in range(1, T + 1):
    # N : 마지막 연결지점 번호, E : 도로 개수
    N, E = map(int, input().split())
    g = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        g[s][e] = w
    result = dijkstra(0, N)
    print(f'#{tc} {result}')