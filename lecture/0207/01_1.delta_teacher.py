# N * N 정사각형의 행렬에서
# 상하좌우의 합 중에 최대값 찾기

arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]


# arr = [[x for x in range(s, s+5)] for s in range(1, 25, 5)]
# 심심해서 만들어본 컴프리헨션으로 만든 2차원 배열


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
