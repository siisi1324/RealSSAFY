# 정수 N, M 이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력하라.
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

# 끝의 N개 만큼 검사해야하므로
    for i in range(N):
        # 오른쪽으로 한칸씩 보내면서 1이랑 검사한다.
        bit_M = (M >> i)
        if bit_M & 0x1 == 0:
            print(f'#{tc} OFF')
            break
            # N번 안에서 하나라도 0이 발견되면 OFF
    else:
        print(f'#{tc} ON')
        # 끝까지 브레이크에 걸리지 않고 통과하면  ON
