# 솔직히 뭐가 틀린지 잘 모르겠지만 간결하게 바꿀 필요성은 느꼈다.
# 이진탐색 이 문제에서 조건 하나는 인지하는게 좋은 것 같다. 오른쪽 페이지보다 왼쪽 페이지가 작은 동안...!

T = int(input())
for tc in range(1, T+1):
    # 끝페이지랑 목표 페이지들 각각 입력받기
    P, A, B = map(int, input().split())

    def find_cnt(p, num):
        # 페이지 넘기는 횟수
        cnt = 0
        # 기준이 되는(계속 바뀌는) 변수 세우기
        l_p = 1
        r_p = p
        standard = (l_p+r_p)//2
        # 그 기준이 목표 페이지와 같아 질 때까지
        while standard != num:
            # 기준 페이지 계속 업데이트시키기
            standard = (l_p+r_p)//2
            # 기준 페이지가 목표보다 작으면 페이지 넘기고, 기준페이지를 왼쪽페이지로 바꾸기
            if standard < num:
                cnt += 1
                l_p = standard
            # 같으면 멈추기
            elif standard == num:
                break
            # 기준 페이지가 목표보다 작으면 페이지 넘기고, 기준페이지를 오른쪽페이지로 바꾸기
            else:
                cnt += 1
                r_p = standard
        return cnt

    A_cnt = find_cnt(P, A)
    B_cnt = find_cnt(P, B)

    # 작은 페이지를 출력시키기, 비기면 0 출력
    if A_cnt < B_cnt:
        print(f'#{tc} A')
    elif A_cnt == B_cnt:
        print(f'#{tc} 0')
    else:
        print(f'{tc} B')