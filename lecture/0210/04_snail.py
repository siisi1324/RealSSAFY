N = 6
arr = [[0] * N for _ in range(N)]
# [0]으로 채워진 6 * 6의 배열을 만든다.
# 현재 위치
r, c = 0, 0
# 달팽이숫자의 방향 순서 : 우하좌상
# dr,dc의 인덱스 의미 >> 0: 우, 1 : 하, 2 : 좌, 3 : 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 오른쪽으로 이동하면서 1,2,3,4,5 넣기
num = 1
d = 0  # 현재 이동방향
while True:
    arr[r][c] = num
    num += 1
    if num == N*N+1:
        break
    r = r + dr[d]
    c = c + dc[d]
    # 범위 벗어나거나, 0 말고 다른 숫자 들어가있으면 방향바꾸기
    if c >= N or r >= N or c < 0 or r < 0 or arr[r][c]:
        r -= dr[d]
        c -= dc[d]
        d = (d + 1) % 4
        r += dr[d]
        c += dc[d]
for row in arr:
    print(row)
print('------------')
