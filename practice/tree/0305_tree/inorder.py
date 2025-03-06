#tree를 중위순회하면서 완성되는 문자열을 반환하는 함수
def solve2(v):
    if v is None:
        return ''
    left_num = tree[v][0]
    right_num = tree[v][1]
    value = tree[v][2]
    left = solve2(left_num)
    right = solve2(right_num)
    return left + value + right

# tree를 중위순회하면서 출력하는 함수
# v: 현재 노드 번호
def solve(v):
    if v is None:   #유효하지 않은 노드라면
        return
    # 중위순회 v번 출력하기 전에 왼쪽 서브트리 먼저...
    # v번 출력하고 나서 오른쪽 서브트리 출력
    # 현재 노드의 정보 >>> tree[v]
    left_num = tree[v][0]
    right_num = tree[v][1]
    value = tree[v][2]
    solve(left_num)
    print(value, end='')
    solve(right_num)


T = 10
for tc in range(1, T + 1):
    N = int(input())  # 정점의 개수 1번부터 N번까지
    # N번 인덱스 까지 활용해야 하므로 N+1 개 생성
    tree = [[None, None, None] for _ in range(N + 1)]
    # 총 N개의 정점 정보를 받기
    for _ in range(N):
        node = input().split()
        num = int(node[0])
        # 노드의 길이가 2또는 3,4
        # node[0] :  현재 정점 번호
        # node[1] : 정점 value(문자열)
        # # node[2] : 왼쪽 자식 번호, # node[3] : 오른쪽 자식 번호
        tree[num][2] = node[1]
        if len(node) >= 3:
            tree[num][0] = int(node[2])
        if len(node) >= 4:
            tree[num][1] = int(node[3])
    print(f'#{tc}',end=' ')
    # solve(1)
    result = solve2(1)
    print(result,end='')
    print()

# 8
# 1 W 2 3
# 2 F 4 5
# 3 R 6 7
# 4 O 8
# 5 T
# 6 A
# 7 E
# 8 S
