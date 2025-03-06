V = int(input())


tree = [[None,None] for _ in range(V+1)]
edges = list(map(int, input().split()))
for i in range(0, (V-1)*2, 2):
    # edges[i] : 부모 edges[i+1] : 자식번호
    # tree의 부모인덱스에 자식 번호가 저장
    if tree[edges[i]][0] is None:
        tree[edges[i]][0] = edges[i+1]
    else:
        tree[edges[i]][1] = edges[i + 1]


for row in tree:
    print(row)
# 13 
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def preorder(v):
    if v is None:
        return
    print(f'{v}번 방문!', end=' ')
    preorder(tree[v][0])
    preorder(tree[v][1])

preorder(1)
# 1번 방문! 2번 방문! 4번 방문! 7번 방문! 12번 방문! 3번 방문! 5번 방문! 
# 8번 방문! 9번 방문! 6번 방문! 10번 방문! 11번 방 문! 13번 방문!