# 숫자 N은 2, 3, 5, 7, 11로 나누어지는 수다. 각각의 지수를 구하라.


T = int(input())

for tc in range(1, T+1):
    num = int(input())
    arr = [0] * 5
    N_arr = [2, 3, 5, 7, 11]


    i = 0
    while num != 1:
        if num % N_arr[i] == 0:
            arr[i] += 1
            num /= N_arr[i]
        else:
            i += 1

    print(f'#{tc}', end=' ')
    for i in arr:
        print(f'{i}', end=' ')
    print()