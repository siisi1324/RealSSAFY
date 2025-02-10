def page_find(p, page):
    cnt = 0
    l = 1
    r = p
    while l <= r: # 검색 구간에 1개 이상의 원소가 있으면 검색
        c = int((l+r)/2) # 기준 위치 계산
        if c == page: # 검색성공
            return cnt
        elif c > page: # 키보다 크면 왼쪽 구간 선택
            r = c 
            cnt += 1
        else: # middle < key, 키보다 작으면 오른쪽 구간 선택
            l = c
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    result_a = page_find(P, A)
    result_b = page_find(P, B)
    if result_a < result_b:
        result = 'A'
    elif result_a > result_b:
        result = 'B'
    else:
        result = '0'

    print(f'#{tc} {result}')

print('=====================================================')

def find_page(end_page, target_page):
    cnt = 0
    start = 1
 
    while start <= end_page:
        find_mid = int((start + end_page) / 2)
        cnt += 1  # 탐색 횟수 증가
 
        if find_mid == target_page:
            return cnt  # 찾았을 때 탐색 횟수 반환
        elif find_mid < target_page:
            start = find_mid  # 오른쪽 탐색
        else:
            end_page = find_mid  # 왼쪽 탐색
 
    return cnt  # 여기까지 올 일은 없음
 
T = int(input())
 
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
 
    cnt_a = find_page(P, Pa)  # A가 몇 번 만에 찾는지
    cnt_b = find_page(P, Pb)  # B가 몇 번 만에 찾는지
 
    # 결과 출력
    if cnt_a < cnt_b:
        print(f'#{tc} A')
    elif cnt_a > cnt_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')