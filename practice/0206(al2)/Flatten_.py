for t in range(10):
    dump_n = int(input())  # 덤프 횟수 입력
    list1 = list(map(int, input().split()))  # 상자 높이 입력

    for _ in range(dump_n):  # 덤프 수행
        # 최댓값, 최솟값 찾기
        max_v = list1[0]
        min_v = list1[0]
        max_index = 0
        min_index = 0

        for i in range(len(list1)):  # 리스트 순회하면서 최댓값, 최솟값 찾기
            if list1[i] > max_v:
                max_v = list1[i]
                max_index = i
            if list1[i] < min_v:
                min_v = list1[i]
                min_index = i

        # 최댓값을 1 감소, 최솟값을 1 증가
        list1[max_index] -= 1
        list1[min_index] += 1

        # 평탄화 완료 시 조기 종료
        if max_v - min_v <= 1:
            break

    # 최종 최댓값과 최솟값 다시 찾기
    max_v = list1[0]
    min_v = list1[0]

    for i in range(len(list1)):  # 리스트 순회하면서 최댓값, 최솟값 찾기
        if list1[i] > max_v:
            max_v = list1[i]
        if list1[i] < min_v:
            min_v = list1[i]

    result = max_v - min_v  # 최종 평탄화 차이 계산
    print(f'#{t+1} {result}')