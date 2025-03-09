# 1984. 중간 평균값 구하기
# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    max_n = 0
    min_n = 10000
    # pop을 사용하려고 인덱스를 구하려고 했는데, 최댓값과 최솟값을 제거하는 과정에서
    # 인덱스 번호가 변경돼서, 값 자체를 삭제하기로 했다. ( remove 사용 )
    # min_index, max_index = 0, 0
    for i in range(10):
        if arr[i] < min_n:
            min_n = arr[i]
            # min_index = i
        if arr[i] > max_n:
            max_n = arr[i]
            # max_index = i
    arr.remove(min_n)
    arr.remove(max_n)
    avg_n = round(sum(arr)/len(arr))
    print(f'#{tc} {avg_n}')