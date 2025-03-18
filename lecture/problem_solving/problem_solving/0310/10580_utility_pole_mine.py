T = int(input())
for tc in range(1, T+1):
    # 전선의 개수 입력받기
    N = int(input())
    # 전선의 시작위치, 끝위치 저장할 배열 만들기
    arr = []
    # 교차점 개수를 저장할 변수 cnt
    cnt = 0
    # N 개의 전선을 입력받으면서
    for i in range(1, N+1):
        # 시작점과 끝점 입력받기
        start, end = map(int, input().split())
        # 먼저 입력받은 점의 위치를 저장하기
        arr.append((start, end))
        # 이미 존재하던 위치들을 꺼내오면서
        for a, b in arr:
            # 입력받은 점과의 비교를 통해서 교차될 때(시작점과 끝점 비교할 때 기호가 다를때)
            if (start < a and end > b) or (start > a and end < b):
                # 교차점은 하나 증가한다.
                cnt += 1
    print(f'#{tc} {cnt}')
