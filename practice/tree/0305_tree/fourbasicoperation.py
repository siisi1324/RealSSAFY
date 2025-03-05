def subtree(root):
    global count
    if root is None:
        return
    count += 1
    subtree(tree[root][0])
    subtree(tree[root][1])


# 부모노드(idx) - 자식노드(왼오)
T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[None, None] for _ in range(E + 2)]
    # tree 작성
    for i in range(0, E * 2, 2):
        if tree[edges[i]][0] is None:
            tree[edges[i]][0] = edges[i + 1]
        else:
            tree[edges[i]][1] = edges[i + 1]
    count = 0
    subtree(N)
    print(f'#{tc} {count}')