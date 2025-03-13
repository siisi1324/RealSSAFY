T = int(input())

for tc in range(1, T + 1):
    # P: 전체 페이지 수, A: A의 목표 페이지, B: B의 목표 페이지
    P, A, B = map(int, input().split())


    # 이진 탐색으로 페이지 찾기
    def find_cnt(p, num):
        cnt = 0
        l_p, r_p = 1, p

        while l_p <= r_p:
            cnt += 1
            mid = (l_p + r_p) // 2

            if mid == num:
                return cnt

            if mid < num:
                l_p = mid
            else:
                r_p = mid

        return cnt


    # 각각 A와 B가 페이지를 찾는데 걸린 횟수
    A_cnt = find_cnt(P, A)
    B_cnt = find_cnt(P, B)

    # 결과 비교 출력
    if A_cnt < B_cnt:
        print(f'#{tc} A')
    elif A_cnt == B_cnt:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')
