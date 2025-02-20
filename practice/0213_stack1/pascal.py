def value(i, j):
    if j == 0 or j == i:  # 첫 번째와 마지막 값은 항상 1
        return 1
    return value(i - 1, j - 1) + value(i - 1, j)
 
def pascal_triangle(N):
    triangle = [[0] * (i + 1) for i in range(N)]  # 미리 리스트를 할당
 
    for i in range(N):
        for j in range(i + 1):
            triangle[i][j] =value(i, j)  # 재귀 함수로 값 채우기
 
    return triangle
 
T = int(input())
for test in range(1, T + 1):
    N = int(input())
    result = pascal_triangle(N)
 
    print(f'#{test}')
    for row in result:
        print(*row)

print('=====================================================')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [[0] * N for _ in range(N)] # 계산이후 넣을 공간
    pascal[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
 
    print(f'#{tc}')
    for k in range(N):
        for m in range(N):
            if pascal[k][m]:
                print(pascal[k][m], end=' ')
        print()