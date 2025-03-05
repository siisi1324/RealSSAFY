T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    Node = E + 1 # 간선 수에 더하기 1한게 노드의 개수
    arr = list(map(int, input().split()))
    cnt = 0

    left = [0] * (Node + 1)  # 부모를 인덱스로 왼쪽자식 저장
    right = [0] * (Node + 1)  # 부모를 인덱스로 오른쪽자식 저장
    par = [0] * (Node + 1)  # 자식을 인덱스로 부모 저장

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        par[p] = c  # 부모를 인덱스로 자식 저장
        if left[p] == 0:  # 왼쪽자식이 아직 없으면
            left[p] = cT = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    Node = E + 1 # 간선 수에 더하기 1한게 노드의 개수
    arr = list(map(int, input().split()))
    cnt = 0

    left = [0] * (Node + 1)  # 부모를 인덱스로 왼쪽자식 저장
    right = [0] * (Node + 1)  # 부모를 인덱스로 오른쪽자식 저장
    par = [0] * (Node + 1)  # 자식을 인덱스로 부모 저장

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        par[p] = c  # 부모를 인덱스로 자식 저장
        if left[p] == 0:  # 왼쪽자식이 아직 없으면
            left[p] = c
        else:  # 왼쪽자식이 있는 경우
            right[p] = c



    def pre_order(T):   # 전위순회, 방문한 정점(부모) 먼저 처리
        global cnt
        if T:   # 0이 아니면 (존재하는 정점이면)
            cnt += 1   # visit(T) T에서 할일 처리
            pre_order(left[T])  # 왼쪽 자식(서브트리)로 이동
            pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동

    pre_order(N)
    print(f'#{tc} {cnt}')

        else:  # 왼쪽자식이 있는 경우
            right[p] = c



    def pre_order(T):   # 전위순회, 방문한 정점(부모) 먼저 처리
        global cnt
        if T:   # 0이 아니면 (존재하는 정점이면)
            cnt += 1   # visit(T) T에서 할일 처리
            pre_order(left[T])  # 왼쪽 자식(서브트리)로 이동
            pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동

    pre_order(N)
    print(f'#{tc} {cnt}')

