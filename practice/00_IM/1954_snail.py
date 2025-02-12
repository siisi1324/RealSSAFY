# N*N식으로 달팽이 숫자 채우기

def solve(arr, n):
    num = 1 # 1부터 시작
    r, c = 0, 0 # 첫번쨰 인덱스 
    dr = [0, 1, 0, -1] # 방향키들
    dc = [1, 0, -1, 0]
    d = 0 # 처음엔 우향
    arr[r][c] = num 
    while num<n*n:
        num +=1 #숫자늘리기 
        r += dr[d] #인덱스변경
        c += dc[d]
        if r>=n or r<0 or c>=n or c<0 or arr[r][c]!=0: # 인덱스범위 및 방향조정 타이밍 설정
            r -= dr[d] # 한보 후진
            c -= dc[d]
            d = (d+1)%4 # 방향키 조정
            r += dr[d] # 다시 전진 
            c += dc[d]
        arr[r][c] = num # 채우기
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    result = solve(arr, N)
    print(f'#{tc}')
    for row in result:
        print(*row) # 공백을 주면서 출력 