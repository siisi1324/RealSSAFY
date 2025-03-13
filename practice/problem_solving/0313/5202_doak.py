def solve(arr):
    cnt = 1
    i = 0
    for j in range(1, len(arr)):
        if

        if arr[j][0] >= arr[i][1]:
            cnt += 1
            i += 1

    return cnt


arr = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append((s, e))
    arr.sort(key=lambda x:x[1])
    result = solve(arr)
    print(f'#{tc} {result}')



