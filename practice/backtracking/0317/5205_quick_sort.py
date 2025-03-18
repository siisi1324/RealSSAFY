# 퀵소트2는 퀵소트2 함수 하나로 해결, 퀵소트 1은 파티션이랑 같이(중간값 찾기)


# 피봇(기준점)을 알려주기 위한 함수임
# 큰 경우와 작은 경우의 요소를 바꿔주는 함수
def partition(s, e):  # hoare 파티션
    # 제일 앞 요소를 pivot_item으로 설정
    pivot_item = arr[s]
    i = s
    j = e
    # 같을 때도 진행하기
    while i <= j:
        # i : 왼쪽에서 오른쪽으로 이동하면서 큰 값찾기
        while i <= j and arr[i] <= pivot_item:
            i += 1
        # j : 오른쪽에서 왼쪽으로 이동하면서 작은 값 찾기
        while i <= j and arr[j] >= pivot_item:
            j -= 1
        # 결국 j가 i보다 더 적아지게 된다. (그럴 때 요소를 바꾸지 않고, while문 탈출하기)
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 탈출한 j(i보다 작아진)와 s(시작점, 피봇) 바꾸기 
    arr[j], arr[s] = arr[s], arr[j]
    # 피봇의 위치만을 알려주기
    return j


# 시작과 종료 범위를 정렬하는 함수
def quick_sort(s, e):
    if s >= e:  # 범위가 역전이 일어나면 정렬할 요소가 없음
        return
    # 파티션 나누고
    pivot = partition(s, e)
    # 작은 쪽 정렬(s 부터 pivot-1)
    quick_sort(s, pivot - 1)
    # 큰 쪽 정렬 (pivot+1 부터 e)
    quick_sort(pivot + 1, e)

#==========================================================================

def quick_sort2(arr):
    if len(arr) < 2:
        return arr
    # 파티션 : 피벗을 기준으로 큰값과 작은값으로 나누기(정렬 X)
    # 피벗은 아무거나 잡으면 되는데...제일 첫 번째 요소로
    pivot_item = arr[0]
    left = []  # 피벗보다 작은 값을 모을 배열
    right = []  # 피벗보다 같거나 큰 값을 모을 배열
    # 피벗으로 잡은 0번 빼고 검사
    for i in range(1, len(arr)):
        if arr[i] < pivot_item:
            left.append(arr[i])
        else:
            right.append(arr[i])
    # 아직 left와 right는 정렬된 상태가 아니니까...정렬하기!
    left = quick_sort2(left)
    right = quick_sort2(right)

    sorted_arr = left + [pivot_item] + right
    return sorted_arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0,N-1)
    # arr = quick_sort2(arr)
    print(f'#{tc} {arr[N // 2]}')