# 수련회에서 원래 방에서 자기 방으로 돌아가려는 과정에서 일어나는 정체를 출력하라

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bokdo = [0] * 201
    for _ in range(1, N+1):
        # s, e = map(int, sorted(input().split()))
        # 입력할 때부터 정렬하는 방법
        s, e = sorted(map(int, input().split()))
        s = (s+1)//2
        e = (e+1)//2
        # 복도에서 일어나는 정체를 더해주기
        for i in range(s, e+1):
            bokdo[i] += 1
	# 가장 많이 정체된 복도를 출력하기(최소 그정도는 시간이 걸린다.)
    print(f'#{tc} {max(bokdo)}')