T = int(input())

for tc in range(1, T+1):
    arr = []
    n = int(input())
    for _ in range(n):
        s, e = map(int, input().split())
        arr.append((s,e))
    arr.sort(key=lambda x: x[1])

    select = []
    prev_end = 0
    for i in arr:
        if i[0] >= prev_end:
            select.append(i)
            prev_end = i[1]

    print(f'#{tc} {len(select)}')

