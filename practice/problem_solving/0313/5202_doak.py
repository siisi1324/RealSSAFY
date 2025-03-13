# 내 코드 ㅎㅎ
def solve(arr):
    cnt = 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j][0] >= arr[i][1]:
            cnt += 1
            i = j

    return cnt



T = int(input())
for tc in range(1, T+1):
    arr = []
    N = int(input())
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append((s, e))
    arr.sort(key=lambda x:x[1])
    result = solve(arr)
    print(f'#{tc} {result+1}')




