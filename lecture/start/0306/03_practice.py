arr = list(input())
L = len(arr)

for i in range(0, L, 7):
    new_arr = list(map(int, arr[i : i+7]))
    num = 0
    for j in range(7):
        if new_arr[j] == 1:
            num += 2**(6-j)
    print(num)


# 0000000111100000011000000111100110000110000111100111100111111001100111