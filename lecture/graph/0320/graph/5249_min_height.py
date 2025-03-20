import heapq


def prim(start):
    pq = [(0, start)]
    MST = [0] * (V + 1)
    min_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(V + 1):
            if graph[node][next_node] == 0:
                continue

            if MST[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))

    return min_weight


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w

    print(f'#{tc} {prim(0)}')