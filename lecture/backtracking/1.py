def merge(arr1, arr2):
    sorted_arr = []
    # 둘 다 존재할 경우에 진행해야 하는 while문이다.
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            sorted_arr.append(arr1.pop(0))
        else:
            sorted_arr.append(arr2.pop(0))

    sorted_arr += arr1
    sorted_arr += arr2
    return sorted_arr



def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    left = arr[:m]
    right = arr[m:]

    left = merge_sort(left)
    right = merge_sort(right)

    sorted_arr = merge(left, right)
    return sorted_arr


arr = [8, 5, 1, 2, 9, 10, 4, 7, 3, 6]
N = len(arr)



print(merge_sort(arr))