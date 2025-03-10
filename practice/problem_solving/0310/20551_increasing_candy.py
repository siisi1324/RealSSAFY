T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    
    # 먹어야 하는 사탕의 개수
    eat_sum = 0
    # A, B, C가 이하면 조건이 성립되지 않는 조건(증가, 0인 박스가 있어선 안 된다.)
    if A < 1 or B < 2 or C < 3:
        print(f'#{tc} -1')
        continue
    # B가 C보다 크면 먹어야 하는 사탕의 개수(B가 C보다 1 작아야 한다.)
    if B >= C :
        eat_sum += B - (C - 1)
        # B 변환
        B = C - 1
    # A가 B보다 크면 먹어야 하는 사탕의 개수(A가 B보다 1 작아야 한다.)
    if A >= B :
        eat_sum += A - (B - 1)
        A = B - 1
    print(f'#{tc} {eat_sum}')
