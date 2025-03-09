def pre_order(N):
    if N:
        print(N)
        pre_order(left[N])
        pre_order(right[N])

N = int(input())
E = N - 1
arr = list(map(int, input().split()))

par=[0]*(N+1)
left = [0] * (N+1)
right = [0] * (N+1)


for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c


root = 1
for i in range(1, N+1):
    if par[i] == 0:
        root = i
pre_order(root)

