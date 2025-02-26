# N*N 크기의 단어퍼즐을 만드려는데, 길이 k를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하라

def solve(arr, n, k):
    total_num = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    total_num += 1
                cnt = 0
        if cnt == k:
            total_num += 1

    return total_num



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(map(list, zip(*arr)))
    # 전치행렬 만드는 법
    result = solve(arr, N, K) + solve(arr2, N, K)
    print(f'#{tc} {result}')
        





