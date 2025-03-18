T = int(input())
for tc in range(1, T+1):
    num = float(input())
    arr = [0]*100
    i = 1
    while num != 0:
        if num * 2 >= 1:
            num = num * 2
            arr[i-1] = 1
            num = num - 1
            i += 1
        else:
            i += 1
            num = num * 2

    if i <= 13:
        print(f'#{tc}', end=' ')
        for c in range(i - 1):
            print(f'{arr[c]}', end='')
        print()
    else:
        print(f'#{tc} overflow')

