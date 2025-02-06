for tc in range(1, 11):
    # 건물의 개수수
    N = int(input())
    data = list(map(int, input().split()))
    print(data)
    # 2번 건물부터 N-3번까지 건물의 조망권 계산
    # 총합을 저장하기 위한 변수
    result = 0
    for i in range(2, N-2):
        # 조망권 계산해서 result에 더해주기
        # 거리 2이내에 있는 건물 살펴보기
        # max_v = data[i-2]
        # if max_v < data[i-1]:
        #     max_v = data[i-1]
        # if max_v < data[i-1]:
        #     max_v = data[i-1]
        # if max_v < data[i-1]:
        #     max_v = data[i-1]
        # if max_v < data[i+2]:
        #     max_v = data[i+2]
        max_v = data[i-2]
        for j in range(i-2, i+3):
            if j == i : continue
            if max_v < data[j]:
                max_v = data[j]
        # max_v : 주변 건물 중 최고 높이
        # 만약 현재 건물 높이가 max_v보다 크면 조망권 세대 있음
        if data[i] > max_v:
            result += data[i] - max_v
    print(f'#{tc} {result}')
