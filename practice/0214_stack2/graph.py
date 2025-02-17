def dfs(v, graph, visited):
    if v == 99:  # 목표 노드 도착
        return True
 
    visited[v] = True
 
    for nxt in graph[v]:
        if not visited[nxt]:  # 아직 방문 안 한 노드만 탐색
            if dfs(nxt, graph, visited):  # 경로를 찾았으면 True 반환
                return True
 
    return False  # 끝까지 가도 못 찾으면 False 반환
 
def solve():
    # 총 10개의 테스트 케이스 처리
    for _ in range(10):
        # 테스트 케이스 번호, 간선 개수 입력
        t, E = map(int, input().split())
 
        # 간선 정보 입력
        edges = list(map(int, input().split()))
 
        # 그래프(인접 리스트) 초기화
        graph = [[] for _ in range(100)]
        for i in range(0, 2 * E, 2):
            start, end = edges[i], edges[i + 1]
            graph[start].append(end)
 
        # 방문 체크 배열
        visited = [False] * 100
 
        # DFS 실행 후 결과 저장
        result = 1 if dfs(0, graph, visited) else 0
 
        # 결과 출력
        print(f"#{t} {result}")
 
solve()