T = int(input())
for tc in range(1, T+1):

    # 배열의 길이 N과 단어의 길이 K를 입력받기
    N, K = map(int, input().split())

    # 배열 입력받기, 배열의 역배열(?)도 입력받기
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_reverse = list(map(list, zip(*arr)))


    def cnt_num(arr):
        # 총 단어가 들어가는 번수 입력
        total_cnt = 0
        for i in range(N):
            # 단어가 들어갈 수 있는 칸 +1 해주기
            cnt = 0
            for j in range(N):
                if arr[i][j] == 1:
                    cnt += 1
                # 동시에 그 칸이 0이거나 N-1(마지막 열)인 경우에, cnt가 K로 존재하고 있으면, total_cnt += 1해주고, cnt는 다시 0으로 바꿔준다.
                if arr[i][j] == 0 or j==N-1 :
                    if cnt == K:
                        total_cnt += 1
                    cnt = 0
        return total_cnt

    num1 = cnt_num(arr)
    num2 = cnt_num(arr_reverse)
    print(f'#{tc} {num1+num2}')
