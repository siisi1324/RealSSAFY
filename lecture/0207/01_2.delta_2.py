arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
K = 2
N = len(arr)

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



# 이건 패턴이므로 외워야 한다. 
# 새로운 방법을 만들자..는 별로