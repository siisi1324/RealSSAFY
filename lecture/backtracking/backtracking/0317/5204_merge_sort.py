
def merge(s, e):
    global cnt
    i = s
    mid = (s + e)//2
    j = mid + 1

    if arr_A[mid] > arr_A[e]:
        cnt += 1

    tmp_arr = []
    while i <= mid and j <= e:
        if arr_A[i] < arr_A[j]:
            tmp_arr.append(arr_A[i])
            i += 1
        else:
            tmp_arr.append(arr_A[j])
            j += 1



    while i <= mid:
        tmp_arr.append(arr_A[i])
        i+=1
    while j<=e:
        tmp_arr.append(arr_A[j])
        j+=1

    for k in range(len(tmp_arr)):
        arr_A[s+k] = tmp_arr[k]




def merge_sort(s, e):
    global cnt
    if s == e:
        return

    m = (s+e)//2
    merge_sort(s, m)
    merge_sort(m+1, e)

    merge(s, e)


T = int(input())
N = int(input())
arr_A = list(map(int, input().split()))
merge_sort(0, N-1)
cnt = 0
mid_num = arr_A[N//2]
print(arr_A)
