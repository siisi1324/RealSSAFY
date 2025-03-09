'''
0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어, 10진수로 출력하기

0000000111100000011000000111100110000110000111100111100111111001100111

answer: 0 120 12 7 76 24 60 121 124 103
'''


# 2진수를 10진수로 변환
def binary_to_decimal(binary_str):
    decimal_number = 0
    power = 0

    # 뒤에서부터 각 자리의 숫자를 10진수로 변환
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** power
        power += 1

    return decimal_number


word = input().strip()

for i in range(0, len(word), 7):
    print(binary_to_decimal(word[i:i+7]), end=' ')



# 내 코드

# 0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어, 10진수로 출력하기

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