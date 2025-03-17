arr = [8, 5, 1, 2, 9, 10, 4, 7, 3, 6]
N = len(arr)

# 인자로 받은 범위에서 병합 실시
# 배열 자체보다 인덱스의 범위를 받는다(배열을 return하는 대신에 인덱스로 직접 다루기)
def merge(s, e):
    # 시작점과 끝점으로 인덱스범위를 나눈다.
    i = s
    mid = (s + e) // 2
    j = mid + 1
    # 비교할 요소가 남아 있으면 비교해라...
    # 임시 배열 tmp_arr에 작은 수부터 append
    tmp_arr = []
    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp_arr.append(arr[i])
            i += 1
        else:
            tmp_arr.append(arr[j])
            j += 1
    # 둘 중 하나는 요소가 없고, 하나는 남아있음
    # 남은거 붙이기
    while i <= mid:
        tmp_arr.append(arr[i])
        i += 1
    while j <= e:
        tmp_arr.append(arr[j])
        j += 1
    # 여기서 원래 배열로 다시 복사해주기
    for k in range(len(tmp_arr)):
        arr[s+k] = tmp_arr[k]
    # 인자로 받은 범위에 있는 요소들 정렬


def merge_sort(s, e):
    # 요소가 하나라면 정렬 필요 X
    if s == e:
        return

    # 인덱스로 배열의 요소가 1개가 될 떄까지 나누기
    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m + 1, e)

    # 나눈 배열을 merge함수로 병합시키기
    merge(s, e)


merge_sort(0, N - 1)
print(arr)
