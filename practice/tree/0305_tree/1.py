N = int(input())

par = [0] * (N+1)
V_arr = [0] * (N+1)
l_arr = [0] * (N+1)
r_arr = [0] * (N+1)


for i in range(N):
    p, V, l, r = 0, 0, 0, 0
    p, V, l, r = input().split()
    p, l, r = int(p), int(l), int(r)
    V_arr[p] = V
    l_arr[p] = l if l != 0 else 0
    r_arr[p] = r if r != 0 else 0

def in_order(T):
    if T:
        in_order(T*2)
        print(f'{V_arr[T]}', end='')
        in_order(T*2+1)


print(in_order(1))






