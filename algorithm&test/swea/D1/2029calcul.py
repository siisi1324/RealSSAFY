def solve(num1, num2):
    v1 = num1 // num2
    v2 = num1 % num2
    print(f'{v1} {v2}')



T = int(input())
for tc in range (1, T+1):
    A, B = map(int, input().split())
    print(f'#{tc} ', end='')
    result = solve(A, B)