def merge(s, e):
    global cnt
    i = s




def merge_sort(s, e):
    if s == e:
        return

    m = (s + e)//2
    merge_sort(s, m)
    merge_sort(m+1, e)
    merge(s, e)




T = int(input())
N = int(input())
arr = list(map(int, input().split()))
cnt = 0
merge_sort(0, N-1)
print(f'#{T} {arr[N//2]} {cnt}')