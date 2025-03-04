# N명, 총 M번의 명령전달
# 난이도(a)는 항상 2, b번의 자리에서 범위 c만큼의 상태를 검사하고 바꾼다.

def solve(m, arr):
    for t_c in range(m):
        a, b, c = map(int, input().split())
        for cc in range(1, c + 1):
            if (b - 1 - cc) >= 0 and (b - 1 + cc) <= N:
                if arr[b - 1 - cc] == arr[b - 1 + cc]:
                    arr[b - 1 - cc] = (arr[b - 1 - cc] + 1) % 2
                    arr[b - 1 + cc] = (arr[b - 1 + cc] + 1) % 2


    return arr


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input().split())
    result = solve(M, arr)
    print(f'#{tc}', *result)

print("====================================================================")

# N명, 총 M번의 명령전달
# 난이도(a)는 항상 2, b번의 자리에서 범위 c만큼의 상태를 검사하고 바꾼다.


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for t_c in range(M):
        a, b, c = map(int, input().split())
        for cc in range(1, c + 1):
            if N> (b - 1 - cc) >= 0 and 0<= (b - 1 + cc) < N:
                if arr[b - 1 - cc] == arr[b - 1 + cc]:
                    arr[b - 1 - cc] = (arr[b - 1 - cc] + 1) % 2
                    arr[b - 1 + cc] = (arr[b - 1 + cc] + 1) % 2

    print(f'#{tc}', *arr)