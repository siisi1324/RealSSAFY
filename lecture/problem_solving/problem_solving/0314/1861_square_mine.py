# 정사각형 방 - 정답 코드
# 접근법
# - N*N visited 배열을 만든다
# - 해당 숫자에서 갈 수 있다면 1을 기록한다
# - 연속된 1의 길이가 가장 긴 곳이 정답이다.
#  - 같은 길이가 있다면, 작은 수가 정답 위치

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    check = [0] * (N * N + 1)

    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    for i in range(N):
        for j in range(N):
            for c in range(4):
                if 0 <= (i + dr[c]) < N and 0 <= (j + dc[c]) < N:
                    new_i = i + dr[c]
                    new_j = j + dc[c]
                    if arr[i][j] + 1 == arr[new_i][new_j]:
                        check[arr[i][j]] = 1
                        break

    start = 0
    total_cnt = 0
    cnt = 0
    for i in range(N * N + 1):
        if check[i]:
            cnt += 1
        else:
            if cnt > total_cnt:
                total_cnt = cnt
                start = i - cnt
            cnt = 0
    print(f'#{tc} {start} {total_cnt + 1}')