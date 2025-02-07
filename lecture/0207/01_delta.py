# 델타를 이용한 2차원 배열 탐색
# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

# 3 * 3의 배열의 인덱스값 (i, j)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# i, j로 묶기가 애매해서 일단 i의 변화량과 j의 변화량을 따로 리스트로 만들어서 인덱스로 튜플로 가져온다. 

N = 2
M = 3

for i in range(N):
    for j in range(M):
        for dir in range(4):
            ni = i +di[dir]
            nj = j +dj[dir]
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)

print('=====================================================')

# 같은 결과
for i in range(N):
    for j in range(M):
        for di, dj in ([0, 1], [1,0], [0,-1], [-1, 0]):
            ni = i +di[dir]
            nj = j +dj[dir]
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)

print('=====================================================')

# 델타 응용
# ex. N*N 배열에서 각 원소를 중심으로, 상하좌우 k칸의 합계 중 최대값(k=2)
max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            for c in range(1, k+1):
                ni, nj = i+di*c, j+dj*c
                if 0<=ni<N and 0<=nj<N:
                    s += arr[ni][nj]
            if max_v < s:
                max_v = s  

print('=====================================================')

# 전치행렬
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
# arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):  # for j in range(i):인 경우우
        if i < j:       # if문 필요없음
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# for i in range(N):
#   f(arr[i][j])

# for i in range(N):
#   f(arr[i][N-1-i])