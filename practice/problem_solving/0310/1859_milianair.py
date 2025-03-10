T = int((input()))
for tc in range(1, T+1):
    # 리스트의 길이
    N = int(input())
    arr = list(map(int, input().split()))

    # 얻을 수 있는 총 이득을 더할 변수
    sum = 0
    # 마지막 요소를 기준으로 for문을 시작한다.
    is_max = arr[N-1]

    for i in range(1, N):
        # 마지막 요소보다 그 전 요소가 작으면 차이를 총 이득의 변수에 더해주고,
        if is_max > arr[N-i-1]:
            sum += (is_max-arr[N-i-1])
        # 그렇지 않으면 다시 그 전의 요소를 기준으로 for문을 돈다.
        else:
            is_max = arr[N-i-1]
    print(f'#{tc} {sum}')