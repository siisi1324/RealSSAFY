# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하라.

# [입력]

# 첫 줄에 테스트 케이스의 수 T가 주어진다. (1 <= T <= 50)
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. (5 <= N <= 1000)
# 다음 줄에 N개의 양수 ai가 주어진다. (1 <= ai <= 1000000)

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

T = int(input()) # 테스트케이스 개수
for tc in range(1, T+1): # 케이스 별로 처리리
    N = int(input()) # 케이스 별 입력 개수
    arr = list(map(int, input().split()))

    max_v = arr[0] # 첫 원소를 최댓값으로 가정
    min_v = arr[0] # 첫 원소를 최솟값으로 가정
    # 조건에서 계산해서 알아서 정해주기

    for i in range(1, N):
        if max_v < arr[i]:   # arr[i] > max_v (다음 연산식과 비교식 순서를 맞출 것)
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
                       

    print(f'#{tc} {max_v-min_v}')