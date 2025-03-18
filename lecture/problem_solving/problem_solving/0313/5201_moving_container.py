def solve(N, M, w_arr, t_arr): # 짐, 트럭, 짐들, 트럭들
    total_sum = 0 # 가능한 짐들 더한거
    i = 0
    for j in range(N):
        if i >= M:
            break
        if t_arr[i] >= w_arr[j]:
            total_sum += w_arr[j]
            i += 1
    return total_sum


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 짐, 트럭
    w_arr = list(map(int, input().split())) # 짐 무게들
    w_arr.sort(reverse=True)
    t_arr = list(map(int, input().split())) # 트럭 적재량
    t_arr.sort(reverse=True)
    result = solve(N, M, w_arr, t_arr)
    print(f'#{tc} {result}')





