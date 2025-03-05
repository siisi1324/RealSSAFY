# 트리 저장은 배열에 할 거에요

tree= [None] * 16
tree[1] = 'A'
tree[2] = 'B'
tree[3] = 'C'
tree[4] = 'D'
tree[6] = 'E'
tree[7] = 'F'
tree[12] = 'G'
tree[13] = 'H'

# 트리의 모든 노드를 순회



# 전위순회 : 루트노드에서 작업처리(방문)하고, 왼쪽서브트리, 오른쪽서브트리 방문하기
# 목표 : V번 노드에서 작업처리하기


def pre_order(v):   
    if v > 15 or tree[v] is None: # 해당번호 노드가 없으면...
        return
    
    # 왼쪽자식(서브트리) : (v * 2)번
    # 오른쪽자식(서브트리) : (v * 2) + 1번
    print(f'{v}번 : {tree[v]}번, ', end=' ')
    pre_order(v*2) # 왼쪽자식 작업처리
    pre_order(v*2+1) # 오른쪽자식 작업처리 

pre_order(1)
# 1번 : A번 2번 : B번 4번 : D번 3번 : C번 6번 : E번 12번 : G번 13번 : H번 7번 : F번 

print()
print("===================================================================")


# 중위순회
def inorder(v):
    if v > 15 or tree[v] is None: # 해당번호 노드가 없으면...
        return
    inorder(v*2)
    print(f'{v}번 : {tree[v]}번, ', end=' ')
    inorder(v*2+1)
inorder(1)
# 4번 : D번,  2번 : B번,  1번 : A번,  12번 : G번,  6번 : E번,  13번 : H번,  3번 : C번,  7번 : F번,

print()
print("===================================================================")

# 후위순회 :
def postorder(v):
    if v > 15 or tree[v] is None: # 해당번호 노드가 없으면...
        return
    postorder(v*2)
    postorder(v*2+1)
    print(f'{v}번 : {tree[v]}번, ', end=' ')

postorder(1)
# 4번 : D번,  2번 : B번,  12번 : G번,  13번 : H번,  6번 : E번,  7번 : F번,  3번 : C번,  1번 : A번,


