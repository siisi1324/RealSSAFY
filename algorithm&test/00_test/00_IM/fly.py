def flapper(row_start, col_start, M, field):  # M과 field를 인자로 받도록 수정
    fly_sum = 0
    
    for row in range(M):
        for col in range(M):
            fly_sum += field[row_start + row][col_start + col]
    
    return fly_sum

T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 크기 N, 파리채 크기 M
    field = [list(map(int, input().split())) for _ in range(N)]
    sum_max = 0
    
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            current_sum = flapper(row, col, M, field)  # sum -> current_sum으로 변경
            
            if sum_max < current_sum:
                sum_max = current_sum
    
    print(f'#{tc} {sum_max}')
