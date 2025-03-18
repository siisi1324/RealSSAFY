# arr이라는 배열에 run 또는 triplet 이 있으면 true를 반환
def check_baby(arr):
    for i in range(10):
        # arr[i] >>> 1개 이상이면 run검사
        # arr[i] >>> 3개 이상이면 triplet
        if arr[i] >= 3:
            return True
        elif arr[i] >= 1:  # 1이상
            if i < 8 and arr[i + 1] >= 1 and arr[i + 2] >= 1:
                return True
    return False


# 게임의 결과를 반환하는 함수
# 비기면 0, 아니면 이긴 선수 반환
def solve():
    # 카드를 선수들에게 한 장씩 나눠 줄건데
    # 카드를 받은 선수는 즉시 check_baby() 실행
    for i in range(12):
        if i % 2:  # i가 홀 수 라면
            p2[cards[i]] += 1
            # true가 반환되면 이긴 선수를 반환
            if check_baby(p2):
                return 2
        else:
            p1[cards[i]] += 1
            if check_baby(p1):
                return 1
    # 모든 카드를 다 나눠 줬는데도... check_baby()가 true를 반환 안하면 비김
    return 0


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    # 각 플레이어의 카드를 저장하는 배열
    p1 = [0] * 10
    p2 = [0] * 10
    result = solve()
    print(f'#{tc} {result}')