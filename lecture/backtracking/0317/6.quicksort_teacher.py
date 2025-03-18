# 정렬 대상 배열을 pivot 기준으로 큰값, 작은값으로 나누는것
# 나뉜값이 정렬된게 아니기 때문에.. 나뉜 값을 다시 정렬
# 인자로 받은 arr 배열을 정렬해서 반환하는 함수
def quick_sort(arr):
    if len(arr) < 2:
        return arr

    # 파티션 : 피벗을 기준으로 큰값과 작은값으로 나누기(정렬x)
    # 피벗은 아무거나 잡으면 되는데...제일 첫번째 요소로
    pivot_item = arr[0]
    left = []  # 피벗보다 작은값을 모을 배열
    right = []  # 피벗보다 같거나 큰 값을 모을 배열
    # 피벗으로 잡은 0번 빼고 검사
    for i in range(1, len(arr)):
        if arr[i] < pivot_item:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # 아직 left와 right는 정렬된 상태가 아니니까...정렬하기!
    left = quick_sort(left)
    right = quick_sort(right)

    sorted_arr = left + [pivot_item] + right
    return sorted_arr


arr = [5, 6, 7, 3, 4, 2, 1, 8, 9]
print(quick_sort(arr))