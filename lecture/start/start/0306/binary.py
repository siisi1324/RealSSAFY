Alphabet = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

# 2진수로 변환


def decimal_to_binary(c):
    binary_number = ""

    if c == 0:
        return '0'

    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while c > 0:
        remainder = c % 2
        binary_number = str(remainder) + binary_number
        c = c // 2

    return binary_number

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()

    total_bin = ''
    for i in num:
        n = Alphabet[i]
        num1 = decimal_to_binary(n)
        if len(num1) < 4:
            num1 = '0' * (4 - len(num1)) + num1
        total_bin += num1

    print(f'#{tc} {total_bin}')