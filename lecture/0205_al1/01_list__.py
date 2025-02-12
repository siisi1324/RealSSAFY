# List

N = int(input())
arr = list(map(int, input().split()))

# 배열원소의 합 s 구하기
s = 0
for i in range(N):
    s += arr[i]

print(s)



