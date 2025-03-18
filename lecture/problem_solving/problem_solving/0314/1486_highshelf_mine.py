# 장훈이의 높은 선반
# N명의 사람들을 쌓아서 B높이가 되는(넘는) 경우를 찾고 그 차이를 출력해라.

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))


    heights = 0 # 각각 for문을 돌릴 때의 높이의 합을 저장할 변수
    height_diff = 20001 # B와 쌓아올린 높이의 차이를 저장할 변수
    for i in range(1<<N): # N명의 부분집합을 만드는 경우
        for j in range(N): # 읽어오면서
            if i & (1<<j): # 겹치면
                heights += arr[j] # 높이에 추가해준다.

        if heights < B: # 쌓아올린 높이가 B보다 크지 않다면 높이를 초기화시키고, 넘긴다.
            heights = 0
            continue
        else:
            if height_diff > heights - B: # B의 높이를 넘긴다면 차이값을 업데이트시킨다.
                height_diff = heights - B
            heights = 0 # 어쨋든 높이는 초기화시킨다.
    print(f'#{tc} {height_diff}')
