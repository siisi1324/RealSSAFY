T = int(input())
for tc in range(1, T + 1):
    # 총 일수
    N = int(input())
    data = list(map(int, input().split()))
    # 1.  최대값 찾고,
    # 2.  시작일 부터 최대값인 일자까지 수익계산하기
    # 반복하면서 시작일이 마지막 날일 때 까지 1,2를 반복
    money = 0  # 총 수익금액

    today = 0
    while today < N:
        max_day = today
        for i in range(today, N):
            # 내가 알고 있는 최대값 일자보다 더 크면 바꿔주기
            if data[max_day] < data[i]:
                max_day = i
        # 오늘부터 최고금액일자 까지 수익계산하기
        for i in range(today, max_day):
            # 수익 : 최고금액 - 오늘금액
            money += data[max_day] - data[i]
        today = max_day + 1

    print(f'#{tc} {money}')


# 내가 하고 싶었던 코드흐름
