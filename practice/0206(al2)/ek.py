T = int(input())

for t in range(1, T+1):
    k, n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))


    cnt = 0 # 충전회수
    wich = 0 # 현재 위치


    while wich + k < n:  # 도착 전에 반복
        for i in range(len(arr1)):  # 충전소 탐색
            if arr1[i] > wich + k:  # 현재 위치에서 이동할 수 없는 충전소 찾기
                wich = arr1[i - 1]  # 그 전 정류장에서 충전
                cnt += 1
                break
        else:
            cnt = 0  # 더 이상 갈 수 있는 충전소가 없는 경우
            break

    print(cnt)
