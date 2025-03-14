# 이전 제출에서 min_v 없이 반환을 하기 위한 코드
def recur(cnt, total):
    if total >= B:  # 재귀하는 동안 목표값(B) 보다 크거나 같다면 최소값 갱신시키기.
        return total - B

    if cnt == N:  # N명 만큼에 대하여 선택했다면 그만.
        return float('inf')

    choose = recur(cnt + 1, total + h_i[cnt])  # 포함 시키는 경우

    no_choose = recur(cnt + 1, total)  # 포함 안하는 경우

    return min(choose, no_choose)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    h_i = list(map(int, input().split()))
    result = recur(0, 0)
    print(f'#{tc} {result}')