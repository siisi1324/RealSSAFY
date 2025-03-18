# 카드를 1회 교환하기
# 1회 교환 할 수 있는 모든 경우의 수를 수행하는 함수
# cnt : 현재 교환한 횟수
def swap(cnt):
    global max_number
    number = int(''.join(cards))
    # 경우의 수를 줄여주기 위해서....
    # 교환횟수와 모양이 같은 경우를 이미 연산해봤으면 연산하지 않음!
    if (cnt, number) in check_set:  # 이미 연산해봤으니까..안함!
        return
    check_set.add((cnt, number))  # 연산할거니까...연산했다고 표시하기

    if cnt == M:  # 지정된 만큼 교환을 완료했으면,
        # 교환 완료했으니....상금이 얼마인지 계산
        if max_number < number:
            max_number = number
        return  # 더이상 교환을 진행하지 않음

    for i in range(N):  # i번 카드부터 교환
        for j in range(i + 1, N):  # i번 카드보다 뒤에 있는 카드들과 교환하기
            # i번 카드와 j번 카드 위치 바꾸기
            # cards[i], cards[j] = cards[j], cards[i]
            tmp = cards[i]
            cards[i] = cards[j]
            cards[j] = tmp
            swap(cnt + 1)  # 다음 순서의 카드 교환을 진행
            # 원래 모양으로 다시 바꾸기
            tmp = cards[i]
            cards[i] = cards[j]
            cards[j] = tmp


def swap2(cnt):
    global max_number
    number = int(''.join(cards))
    # 경우의 수를 줄여주기 위해서....
    # 교환횟수와 모양이 같은 경우를 이미 연산해봤으면 연산하지 않음!
    if (cnt, number) in check_set:  # 이미 연산해봤으니까..안함!
        return 0
    check_set.add((cnt, number))  # 연산할거니까...연산했다고 표시하기

    if cnt == M:  # 지정된 만큼 교환을 완료했으면,
        return number

    max_result = 0
    for i in range(N):  # i번 카드부터 교환
        for j in range(i + 1, N):  # i번 카드보다 뒤에 있는 카드들과 교환하기
            # i번 카드와 j번 카드 위치 바꾸기
            # cards[i], cards[j] = cards[j], cards[i]
            tmp = cards[i]
            cards[i] = cards[j]
            cards[j] = tmp
            max_result = max(max_result, swap2(cnt + 1))  # 다음 순서의 카드 교환을 진행
            # 원래 모양으로 다시 바꾸기
            tmp = cards[i]
            cards[i] = cards[j]
            cards[j] = tmp
    return max_result

T = int(input())
for tc in range(1, T + 1):
    # 입력 형태가 123 1  >>> ['1','2','3']  1
    cards, M = input().split()
    N = len(cards)  # 숫자 카드의 개수
    M = int(M)  # 카드 교환 횟수
    cards = list(cards)
    # max_number = 0
    # 교환 횟수와 카드 모양을 저장해서 연산해봤는지 확인하기
    check_set = set()
    # swap(0)
    max_number = swap2(0)
    print(f'#{tc} {max_number}')
