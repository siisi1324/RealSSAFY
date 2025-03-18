T = int(input())
N = int(input())

arr = list(map(int, input().split()))

now = 0
start = now
sum = 0
for i in range(start, N+1):
    if arr[now] < arr[i]:
        sum += arr[i] - arr[now]
    else:
        start = now+1
print(sum)