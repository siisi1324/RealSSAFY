# 가격이 쌀 때사서 비쌀 때 팔자주의

T = int(input())
N = int(input())
arr = list(map(int, input().split()))
L = len(arr)

while True:
    i = 0
    sum = 0
    num1 = arr[i]
    for index in range(i+1, L):
        if arr[index] > num1:
            a_index = index
            for index2 in range(i, a_index):
                sum += (arr[index2] - num1)
        else:
            break

    print(sum)
    break

