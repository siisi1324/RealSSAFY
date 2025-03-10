# <연습문제 1> 0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어, 10진수로 출력하기

arr = list(input())
L = len(arr)

for i in range(0, L, 7):
    new_arr = list(map(int, arr[i : i+7]))
    num = 0
    for j in range(7):
        if new_arr[j] == 1:
            num += 2**(6-j)
    print(num, end=' ')


# 0000000111100000011000000111100110000110000111100111100111111001100111

