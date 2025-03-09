import sys
sys.stdin = open("input.txt", "r")

# M의 우측 N개를 확인 (반복문을 활용한 방법)
# - 하나라도 0이 나오면 False
def solution():
    target = M
    # N 번 확인한다.
    for _ in range(N):
        # 맨 우측 비트가 1인 지 체크
        # 0x1, 0b1, 1 다 사용 가능
        # - 0x1: 비트 연산이라는 것을 명시하기 위해 사용
        if target & 0x1 == 0:
            return False
        # 맨 우측 비트를 삭제
        target = target >> 1
    return True


# 업그레이드 버전
def solution():
    # N 개의 1 을 구함
    # 16(10000) - 1 = 1111
    mask = (1 << N) - 1
    result = (M & mask) == mask
    return result

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = solution()


# 내 버전
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