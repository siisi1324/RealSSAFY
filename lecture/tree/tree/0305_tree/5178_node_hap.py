T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    # L_arr = [0] * (N+1)
    # R_arr = [0] * (N+1)

    # 인덱스번호에 값만 넣어주기(완전 이진트리)
    par = [0] * (N + 1)
    for i in range(M):
        index, V = map(int, input().split())
        par[index] = V


    # 재귀로 부모 노드에 자식노드들의 합을 넣어주기
    def pre_order_hap(T):
        # 인덱스 범위가 초과하거나 이미 값이 있는 경우에는 그대로 par[T]반환
        if par[T] != 0:
            return par[T]
        # 각각 왼쪽 노드와 오른쪽 노드들을 불러오기(재귀)
        left = pre_order_hap(T * 2) if T * 2 <= N else 0
        right = pre_order_hap(T * 2 + 1) if T * 2 + 1 <= N else 0
        par[T] = left + right
        return par[T]


    # L(원하는 노드번호) 이하부터 노드 채우기
    pre_order_hap(L)
    # 노드 값 출력
    print(f'#{tc} {par[L]}')
