# 트리를 후위 순회 하면서 연산
# v번노드에 숫자가 들어가 있을 수 도 있고...연산자가 들어있을 수도 있음
def solve2(v):
    node_value = tree[v][2]
    if node_value.isdigit():
        return int(node_value)
    #연산하기 전에...... 왼쪽 자식 오른쪽 자식 먼저 연산
    left_num = tree[v][0]
    right_num = tree[v][1]
    left_result = solve2(left_num)
    right_result = solve2(right_num)
    #루트 노드 처리
    if node_value == '+':
        return left_result + right_result
    elif node_value == '-':
        return left_result - right_result
    elif node_value == '*':
        return left_result * right_result
    else:
        return left_result / right_result




def solve(v):
    if v is None:
        return
    node_value = tree[v][2]
    #연산하기 전에...... 왼쪽 자식 오른쪽 자식 먼저 연산
    left_num = tree[v][0]
    right_num = tree[v][1]
    solve(left_num)
    solve(right_num)
    #루트 노드 처리
    if node_value in '+-*/':    #연산자라면
        if node_value == '+':
            # 왼쪽 서브트리의 결과  +
             tree[v][2] = tree[left_num][2] + tree[right_num][2]
        elif node_value == '-':
            tree[v][2] = tree[left_num][2] - tree[right_num][2]
        elif node_value == '*':
            tree[v][2] = tree[left_num][2] * tree[right_num][2]
        else:
            tree[v][2] = tree[left_num][2] / tree[right_num][2]

    else:
        tree[v][2] = int(tree[v][2])

T = 10
for tc in range(1,T+1):
    N = int(input())
    tree = [[None,None,None] for _ in range(N+1)]
    for _ in range(N):
        # 노드번호만 숫자로 저장, 피연산자 및 연산자는 문자열로 저장
        node = input().split()
        num = int(node[0])
        tree[num][2] = node[1]
        if len(node) == 4:
            tree[num][0] = int(node[2])
            tree[num][1] = int(node[3])

    # solve(1)
    # print(f'#{tc} {int(tree[1][2])}')
    result = int(solve2(1))
    print(f'#{tc} {result}')


    #제대로 입력받았는지 확인
    # for row in tree:
    #     print(row)


# 5
# 1 - 2 3
# 2 - 4 5
# 3 10
# 4 88
# 5 65