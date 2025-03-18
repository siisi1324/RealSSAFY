def dfs(i, prob, visited):
    global answer

    if prob <= answer:  # 가지치기 (Pruning)
        return

    if i == N:  # 모든 행을 확인한 경우
        answer = prob  # 최대 확률 업데이트
        return

    for j in range(N):  # 가능한 모든 열(작업) 탐색
        if j not in visited:  # 아직 선택되지 않은 경우만 진행
            visited.add(j)
            dfs(i + 1, prob * (table[i][j] / 100), visited)
            visited.remove(j)  # 백트래킹

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N = int(input())  # 직원 수 = 작업 수
    table = [list(map(int, input().split())) for _ in range(N)]  # 확률 테이블 입력

    answer = 0  # 최대 확률 초기화
    dfs(0, 1, set())  # 탐색 시작

    print(f'#{tc} {answer * 100:.6f}')  # 결과 출력
