# x나 y중 둘 중 하나 이상에 저장된 값이 N초과가 되게 위해서 최소 연산을 몇 번 수행해야 하는지 출력하라.

T = int(input())
for tc in range(1, T+1):
    A, B, N = map(int, input().split())
    cnt = 0
    while A <= N or B <= N:
        cnt += 1
        if A<B:
            A += B
        else:
            B += A
    print(cnt-1)