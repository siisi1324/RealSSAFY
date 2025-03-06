# 함수를 쓰면 되지만 할 줄 알아야 한다.
# 뭐든지


# 2진수로 변환
def decimal_to_binary(n):
    binary_number = ""

    if n == 0:
        return "0"

    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remainder = n % 2
        binary_number = str(remainder) + binary_number
        n = n // 2

    return binary_number


# 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""

    if n == 0:
        return "0"

    # 0보다 클 때까지 16으로 나누면서 나머지를 정답에 추가
    while n > 0:
        remainder = n % 16
        hexadecimal_number = hex_digits[remainder] + hexadecimal_number
        n = n // 16

    return hexadecimal_number


# 2진수를 10진수로 변환
def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    # 뒤에서부터 각 자리의 숫자를 10진수로 변환
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
        pow += 1

    return decimal_number


# 16진수를 10진수로 변환
def hexadecimal_to_decimal(hex_str):
    hex_digits = "0123456789ABCDEF"
    decimal_number = 0
    pow = 0

    # 뒤에서부터 각 자리의 숫자를 10진수로 변환
    for digit in reversed(hex_str):
        decimal_number += hex_digits.index(digit.upper()) * (16 ** pow)
        pow += 1

    return decimal_number

# hex_to_decimal
# 16진수 알파벳이 어떤 숫자를 의미하는지 계산
hex_dict = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
}
# hex_to_decimal
# 16진수 알파벳이 어떤 숫자를 의미하는지 계산
def hex_to_decimal(hex_num):    #'4F1A'
    exp = len(hex_num)-1
    # 16의 지수승 들을 더할 변수
    decimal_num = 0
    for i in range(len(hex_num)):
        # hex_dict[hex_num[i]] : 10진 숫자
        decimal_num += (16**exp * hex_dict[hex_num[i]])
        exp -= 1
    return decimal_num

def decimal_to_binary(num):
    binary = ''
    while num > 0:
        remain = num % 2
        num = num // 2
        binary = str(remain) + binary
    return binary

print(hex_to_decimal('47FE'))
print(decimal_to_binary(20))
print(decimal_to_binary(hex_to_decimal('47FE')))
# 0100011111111110
 # 100011111111110




# 예시: 10진수를 2진수와 16진수로 변환
decimal_num = 16
binary_num = decimal_to_binary(decimal_num)
hex_num = decimal_to_hexadecimal(decimal_num)

print(f"{decimal_num} - 2진수: {binary_num}")
print(f"{decimal_num} - 16진수: {hex_num}")
print('--------------------------')

binary_to_decimal_num = binary_to_decimal(binary_num)
hexadecimal_to_decimal_num = hexadecimal_to_decimal(hex_num)

print(f"{binary_num} - 10진수: {binary_to_decimal_num}")
print(f"{hex_num} - 10진수: {hexadecimal_to_decimal_num}")
