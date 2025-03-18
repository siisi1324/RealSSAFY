# 병합정렬 : 전체를 정렬하기 위해서
# 정렬된 두 개를 합치는 알고리즘
arr = [8, 5, 1, 2, 9, 10, 4, 7, 3, 6]
N = len(arr)


# 정렬된 두 배열을 병합해서 반환하는 함수
def merge(arr1, arr2):
    sorted_arr = []
    # 둘 중에 하나라도 끝나면 false가 된다.
    while arr1 and arr2:
        # arr1[0], arr2[0] 끼리 비교
        if arr1[0] < arr2[0]:
            # 삭제하면서 새로 arr업데이트하기
            sorted_arr.append(arr1.pop(0))
        else:
            sorted_arr.append(arr2.pop(0))
    # 작은거 비교 하는게 끝나면....둘 중 하나는 남을건데...
    # 남은거 다 붙이기
    sorted_arr += arr1
    sorted_arr += arr2
    return sorted_arr

# 리스트를 인자로 받아서, 정렬해서 반환하는 함수
# 병합 : 정렬된 작은 두 배열을 합치는 과정   [1,4,6] , [2,3,5]
#           >>>>> [1,2,3,4,5,6]
def merge_sort(arr):
    if len(arr) == 1:  # 요소가 하나라면 정렬된 상태라고 볼 수 있음
        return arr
    m = len(arr) // 2  # 중간 인덱스
    left = arr[:m]
    right = arr[m:]
    # left, right 가 정렬된 상태가 아니니까..정렬
    left = merge_sort(left)
    right = merge_sort(right)

    sorted_arr = merge(left, right)
    return sorted_arr


print(merge_sort(arr))
