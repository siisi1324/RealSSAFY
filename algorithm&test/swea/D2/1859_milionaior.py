# 가격이 쌀 때사서 비쌀 때 팔자주의

# Testcase
T = int(input())
for tc in range(1, T+1):
    # 각 날의 매매가를 나타내는 N개의 자연수
    N = int(input())
    arr = list(map(int, input().split()))
    L = len(arr)


    is_max = arr[L-1]
    sum = 0
    for i in range(L-2, -1, -1):
        if arr[i] < is_max:
            sum += is_max - arr[i]
        else:
            is_max = arr[i]

    print(f'#{tc} {sum}')



















# 스웨아 풀이 베껴옴

# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     data = list(map(int, input().split()))
#
#     result = 0
#     val = data[N - 1]
#     for i in range(N - 2, -1, -1):
#         if data[i] < val:
#             result += val - data[i]
#         elif data[i] >= val:
#             val = data[i]
#     print(f'#{t} {result}')