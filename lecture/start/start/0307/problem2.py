# <연습문제 2>
# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해 보자.
N_str = list(input())

# 01D06079861D79F99F
# 0F97A3


hex_to_bin_map = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
total_str = ''
for i in N_str:
    I = hex_to_bin_map[i]
    total_str += I

L = len(total_str)

for i in range(0, L, 7):
    arr = list(map(int, total_str[i:i+7]))
    sum = 0
    for j in range(len(arr)):
        if arr[j]==1:
            sum += 2**(len(arr)-j-1)
    print(sum, end=' ')
