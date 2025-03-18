# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total_arr = sorted(arr)
    print(f'#{tc}', *total_arr)

