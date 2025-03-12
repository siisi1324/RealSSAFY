path = []
arr = list(map(int, input().split()))
arr_cnt = [0 for _ in range (6)]


def is_babygin(bath):
    for i in range(6):
        if arr_cnt[i] >= 3:
            for _ in range(arr_cnt[i]):
                arr.remove(arr[i])
            return

    path1 = sorted(path)
    if





def solve(num):
    if num == 6:
        if is_babygin(path):
            print(True)
        else:
            print(False)



    for i in range(6):
        arr_cnt[i] += 1
        path.append(arr[i])
        solve(num+1)
        path.pop()
        arr_cnt[i] -= 1

solve(0)