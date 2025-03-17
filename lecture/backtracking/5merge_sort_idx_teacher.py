arr = [8, 5, 1, 2, 9, 10, 4, 7, 3, 6]
N = len(arr)

# 인자로 받은 범위에서 병합 실시
def merge(s, e):
    i = s
    mid = (s + e) // 2
    j = mid + 1
    # 비교할 요소가 남아 있으면 비교해라...
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

    for k in range(len(tmp_arr)):
        arr[s+k] = tmp_arr[k]
    # 인자로 받은 범위에 있는 요소들 정렬


def merge_sort(s, e):
    # 요소가 하나라면 정렬 필요 X
    if s == e:
        return

    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m + 1, e)
    merge(s, e)


merge_sort(0, N - 1)
print(arr)
