def decimal_to_binary(n):
    word = ''
    while n != 0:
        plus_w = n%2
        word = str(plus_w) + word
        n //= 2
    return word

# print(decimal_to_binary(5))

def decimal_to_heximal(n):
    hex_digit = '0123456789ABCDEF'
    hex_word = ''

    while n != 0:
        plus_v = n%16
        hex_word = hex_digit[plus_v] + hex_word
        n //= 16
    return hex_word

# print(decimal_to_heximal(256))

def binary_to_decimal(int_n):
    num = 0
    i = 0
    while int_n!=0:
        boot = int_n%10
        if boot == 1:
            num += 2**i
        i += 1
        int_n //= 10
    return num

# print(binary_to_decimal(1101))

def binary_to_decimal2(int_str):
    num = 0
    pow = 0
    for i in reversed(int_str):
        if i == '1':
            num += 2**pow
        pow+=1
    return num
# print(binary_to_decimal2('1101'))

hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
def hexa_to_decimal(hex_str):
    num = 0
    pow = 0
    for i in reversed(hex_str):
        if i in hex_dict:
            num += (16**pow)*hex_dict[i]
        pow+=1
    return num

# print(hexa_to_decimal('47FE'))

