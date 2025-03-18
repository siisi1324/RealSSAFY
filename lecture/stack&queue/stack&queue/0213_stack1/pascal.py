# 자빈언니코드

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


print('=====================================================')
# 함수형으로 수정(return, 0인 값 제외시키기)

def solve(N):
    pascal = [[0] * N for _ in range(N)] # 계산이후 넣을 공간
    pascal[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal  # 반환 추가

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = solve(N)  # 함수에서 삼각형을 받아옴
    print(f'#{tc}')
    for row in result:
        print(*[num for num in row if num])  # 0이 아닌 값만 출력
