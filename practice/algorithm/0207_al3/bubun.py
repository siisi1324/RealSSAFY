A = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

T = int(input())

for i in range(T):
    cnt = 0
    N, K = map(int, input().split())
    total_set = []
    for j in range(1<<len(A)):
        subset = []
        for k in range(len(A)):
            if (1<<k) & j:
                subset.append(A[k])
        total_set.append(subset)
        # 모든 부분집합 만들기

    for li_st in total_set:
        if sum(li_st)==K and len(li_st)==N:
            cnt += 1

    print(f'#{i+1} {cnt}')

print('=====================================================')

# 김해민 언니 코드 
A = [x for x in range(1, 13)]  # 집합 A : 1~12까지 원소 가짐
T = int(input())
for tc in range(1, T + 1):
    # N : 부분집합 원소의 수, K : 부분집합의 합
    N, K = map(int, input().split())
    cnt = 0     # 부분집합 개수
    for i in range(1 << 12):    # 집합 A의 길이 : 12
        sub_set_ls = []  # 부분집합 원소 담을 리스트
        sum_v = 0  # 부분집합의 합
        for j in range(12):
            if i & 1 << j:
                sub_set_ls.append(A[j])     # 부분집합 리스트에 원소 추가
                sum_v += A[j]       # 부분집합의 합 구하기

        # 부분집합의 길이(원소 개수)와 sum_v가 입력받은 N과 K와 같으면
        if len(sub_set_ls) == N and sum_v == K:
            cnt += 1        # 개수 증가
    print(f'#{tc} {cnt}')


print('=====================================================')

# subset 없애고 비교적 최적화한 코드
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  

T = int(input()) 

for tc in range(1, T + 1):  
    N, K = map(int, input().split())  # N: 부분집합 크기, K: 부분집합 합 목표값
    result = 0  # 조건을 만족하는 부분집합 개수 저장

    # 모든 부분집합 탐색 (비트마스크 활용)
    for i in range(1 << len(A)):  
        sum_v = 0  # 부분집합의 합
        count = 0  # 선택한 원소 개수

        for j in range(len(A)):  # A의 원소(12개)에 대해 비트를 확인
            if i & (1 << j):  # i의 j번째 비트가 1이면 해당 원소 포함
                sum_v += A[j]  # 바로 합 계산
                count += 1  # 원소 개수 카운트

        # 부분집합 크기(N)와 합(K) 조건을 동시에 체크
        if count == N and sum_v == K:
            result += 1  # 조건을 만족하는 경우 카운트 증가

    print(f'#{tc} {result}')  # 테스트 케이스 번호와 결과 출력

# 연습필요..!!
# 필수까지는 아니고,,(비트연산)
# 백트래킹도 안된다고 한다. 
# 이해는 하시되, 집착은 마시라..