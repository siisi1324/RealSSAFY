arr = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 14, 15, 16, 17, 20, 25, 30]

# arr : 탐색 대상
# start :탐색 시작 인덱스
# end : 탐색 종료 인덱스
# key : 찾을 값
def binary_search(arr, start, end, key):
    while start <= end:  # start, end의 범위를 재지정하면서 반복
        # 만약 start,end의 값이 역전되면 범위 성립이 안됨 >> 탐색실패
        # if start > end:
        #     break  # 탐색 종료
        mid = (start + end) // 2
        # 중간 값 비교
        if arr[mid] == key:
            return True  # key가 대상 안에 있음!
        elif arr[mid] > key:  # 중간값은  key가 아니니까 큰지 작은지 비교
            # 중간 값보다 큰 영역은 볼 필요가 없음
            end = mid - 1
        else:  # arr[mid] < key
            start = mid + 1
    # 반복적으로 값을 찾았지만 key를 찾지 못함
    return False

# 지정한 영역 내에 key값이 있으면 True 없으면 False를 반환
def binary_search_recursive(arr, start, end, key):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] == key:
        return True
    elif arr[mid] > key:    # 중간 이후 영역은 볼 필요가 없음
        return binary_search_recursive(arr, start, mid-1, key)
    else:
        return binary_search_recursive(arr, mid+1, end, key)

# print(binary_search(arr, 0, len(arr) - 1, 11))
print(binary_search_recursive(arr,0,len(arr)-1,21))
