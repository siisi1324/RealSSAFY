# 구간의 시작인덱스부터 잡아주기
# 0에서 시작하는 구간, 1번에서 시작하는 구간, 2번에서 시작하는 구간
# min_v = sum(arr[:M])
# max_v = sum(arr[:M])

T = int(input()) # 테스트케이스 개수
N, M = map(int, input().split())
arr = list(map(int, input().split()))
for tc in range(1, T+1): # 케이스 별로 처리리
    min_v = 1000000
    # 임의로 마음대로 걍 잡기(조건보고)
    max_v = 0
    for i in range(N-M+1):
        # i 번에서 시작하는 길이 M짜리 구간 반복
            sum_v += arr[j]
            if sum_v > max_v:
                max_v = sum_v
            if sum_v < min_v :
                min_v = sum_v
    print(f'{max_v-min_v}')


    T = int(input())  # 테스트 케이스 개수 입력
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 배열 크기, M: 부분 배열 크기
    arr = list(map(int, input().split()))  # 배열 입력 받기

    min_v = float('inf')  # 최소값 초기화
    max_v = float('-inf')  # 최대값 초기화

    for i in range(N - M + 1):  # 가능한 부분 배열 시작 인덱스
        sum_v = sum(arr[i:i+M])  # 부분 배열 합 계산

        if sum_v > max_v:
            max_v = sum_v
        if sum_v < min_v:
            min_v = sum_v

    print(f'#{tc} {max_v - min_v}')  # 최대-최소 차이 출력



# min, max, sum, count, index 압수..
# 코드 한줄한줄에 이유가 있어야 한다. (주석으로 남기기)