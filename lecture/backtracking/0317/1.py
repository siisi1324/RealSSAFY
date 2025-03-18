def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_item = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot_item:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = quick_sort(left)
    right = quick_sort(right)

    sorted_arr = left + [pivot_item] + right
    return sorted_arr



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = quick_sort(arr)
    print(f'#{tc} {arr[N//2]}')

