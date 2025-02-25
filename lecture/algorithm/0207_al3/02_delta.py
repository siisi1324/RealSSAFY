# N * N 정사각형의 행렬에서
# 상하좌우의 합 중에 최대값 찾기

arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
print('=====================================================')


# arr = [[x for x in range(s, s+5)] for s in range(1, 25, 5)]
# 심심해서 만들어본 컴프리헨션으로 만든 2차원 배열


print('=====================================================')


# 이건 그냥 순회
N = len(arr)

for i in range(N):
    # print(arr[i]) : 리스트
    for j in range(N): # i행의 j번 요소 출력
        # 각 요소마다 상하좌우에 있는 요소에 접근
        # 현재좌표 (i, j)
        print(arr[j][i]) # 열 우선순회
        print(arr[i][j]) # 행 우선순회

print(arr)

print('=====================================================')

# 이건 델타
# 상하좌우 4방향에 접근을 위해서 변화량배열(델타) 선언
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 4방향 합 구하기
for r in range(N):
    # print(arr[i]) : 리스트트
    for c in range(N): # i행의 j번 요소 출력
        # 각 요소마다 상하좌우에 있는 요소에 접근
        # d : 방향을 나타내는 변수, 0 : 상. 1 : 하, 2 : 좌, 3 : 우
        sum_v = arr[r][c]
        for d in range(4):
            # 현재좌표 (r,c)
            # 보려는 좌표
            # 여기에 반복문 한번들어가야함...
            nr = r + dr[d]
            nc = c + dc[d]
            # if (nr >= 0 and nr < N) and (nc >= 0 and nc < N):
            if 0 <= nr < N and 0 <= nc < N:
                # nr과 nc가 정상범위
                sum_v += arr[nr][nc]
        print(sum_v)


print('=====================================================')

# 여기는 각 델타에서 k개씩만큼 더하기를 할 떄를 구하는 법
K = 2

# 4방향 합 구하기
for r in range(N):
    # print(arr[i]) : 리스트트
    for c in range(N): # i행의 j번 요소 출력
        # 각 요소마다 상하좌우에 있는 요소에 접근
        # d : 방향을 나타내는 변수, 0 : 상. 1 : 하, 2 : 좌, 3 : 우
        sum_v = arr[r][c]
        for d in range(4):
            for a in range(1, K+1):
                # 현재좌표 (r,c)
                # 보려는 좌표
                # 여기에 반복문 한번들어가야함...
                nr = r + dr[d] * a
                nc = c + dc[d] * a
                # 매 d 마다 원래 위치로 돌아가므로 걱정 ㄴㄴ
                # if (nr >= 0 and nr < N) and (nc >= 0 and nc < N):
                if 0 <= nr < N and 0 <= nc < N:
                    # nr과 nc가 정상범위
                    sum_v += arr[nr][nc]
        print(sum_v)
# 한번에 갈때 2칸씩 받으면 되는게 있고, 회오리 두번 돌리는게 있다. 
# d문과 a문의 위치를 바꾸면 해결된다.
        

# 이거는 같은 방식으로 K만큼 더한 값 중에 최댓값 찾긴
max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            for c in range(1, K+1):
                ni, nj = i+di*c, j+dj*c
                if 0<=ni<N and 0<=nj<N:
                    s += arr[ni][nj]
            if max_v < s:
                max_v = s  
        

print('=====================================================')

# 이건 패턴이므로 외워야 한다. 
# 새로운 방법을 만들자..는 별로

print('=====================================================')

# 전치행렬
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
# arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):  # for j in range(i):인 경우우
        if i < j:       # if문 필요없음
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in range(3):
    for j in range(i):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        # 다만 그 위치를 바꾸는 주체 자체는 다르다. 
        # 위에 코드는 왼쪽하반부, 밑에 코드는 오른쪽상반부ㅋㅋ( >, <에 따라 다르긴 하다. )


for i in range(N):
  f(arr[i][j])
# 우하향 대각선  
  

for i in range(N):
  f(arr[i][N-1-i])
# 우상향 대각선
            
print('=====================================================')

# 얘는 대각선 두개의 합을 구하는 방법(중앙값 빼기)
# <연습문제 1>

s = 0
for i in range(5):
    s += arr[i][i]
    s += arr[i][4-i]

s-=arr[5//2][5//2]


print('=====================================================')

# <연습문제 2>
# 5*5 2차 배열에 25개의 숫자를 저장하고, 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    for j in range(N):
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N:
                total += abs(arr[ni][nj]- arr[i][j])
print(total)