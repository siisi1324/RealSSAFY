T = int(input())  # 테스트 케이스 개수 입력

for t in range(1, T+1):
    k, n, m = map(int, input().split())  # k: 이동 가능 거리, n: 종점, m: 충전소 개수
    arr1 = list(map(int, input().split()))  # 충전소 위치

    cnt = 0  # 충전 횟수
    wich = 0  # 현재 위치

    # **두 정류장 사이 거리가 k보다 크면 0 출력 후 종료**
    for i in range(1, len(arr1)):  
        if arr1[i] - arr1[i - 1] > k:
            cnt = 0
            break

    # 정상적인 경우, 충전 시작
    else:
        while wich + k <= n:  # 도착 전까지 반복
            for i in range(len(arr1)):  # 충전소 탐색
                if arr1[i] < wich: continue
                if arr1[i] - wich > k:  # 현재 위치에서 이동 가능한 범위를 초과하는 충전소 발견
                    wich = arr1[i-1]  # 직전 충전소에서 충전
                    cnt += 1
                    break
            else:  # 더 이상 이동할 충전소가 없는 경우
                cnt = 0
                break

    print(f'#{t} {cnt}')

# for - else 
# for 문에서 브레이크가 한번도 실행이 안되면, else로 간다.