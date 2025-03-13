

def solve(n, m, arr1, arr2):
    total_sum = 0
    i = 0
    for j in range(N):
        if t_arr[j] >= w_arr[i]:
            total_sum += w_arr[i]
            i += 1
        return total_sum








T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w_arr = list(map(int, input().split()))
    w_arr.sort(reverse=True)
    t_arr = list(map(int, input().split()))
    t_arr.sort(reverse=True)
    result = solve(N, M, w_arr, t_arr)
    print(f'{tc} {result}')





