def find_num(N, memo):
    if N == 1:
        return 1
    if N == 2:
        return 3
     
    if memo[N]:  # 0이 아니면 이미 계산된 값
        return memo[N]
     
    # 점화식: 이전 값 + (두 칸 전 값 * 2)
    memo[N] = find_num(N - 1, memo) + find_num(N - 2, memo) * 2
    return memo[N]
 
# 테스트 케이스 개수
T = int(input())
 
for t in range(1, T + 1):
    # 입력값 N을 10으로 나눈 값으로 처리 (단위 변환)
    N = int(input()) // 10  
 
    # 메모이제이션 배열 초기화
    memo = [0] * (N + 1)
 
    # 결과 계산
    result = find_num(N, memo)
 
    # 결과 출력
    print(f"#{t} {result}")