# 정렬된 두 배열을 병합해서 반환하는 함수
def merge(s, e):
    global cnt
    i = s
    mid = (s + e - 1) // 2
    j = mid + 1
    # 비교할 요소가 남아 있으면 비교해라...
    if arr[mid] > arr[e]:
        cnt += 1

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
        arr[s + k] = tmp_arr[k]
    # 인자로 받은 범위에 있는 요소들 정렬


def merge_sort(s, e):
    # 요소가 하나라면 정렬 필요 X
    if s == e:
        return

    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m + 1, e)
    merge(s, e)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge_sort(0, N - 1)
    # arr = merge_sort(arr)
    print(f'#{tc} {arr[N // 2]} {cnt}')