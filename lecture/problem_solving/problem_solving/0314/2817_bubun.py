T = int(input())
N, K = map(int, input().split())
arr = list(map(int, input().split()))
n = len(arr)
cnt = 0

for i in range(1<<n):
    if i & 0x1



# 부분집합 개수

arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)
answer = 0


def get_count(target):  # 총 몇개의 비트가 1인지 체크
    cnt = 0
    for i in range(n):
        if target & 0x1:  # 비트가 1이라면
            # if (tar>>i) & 0x1:
            cnt += 1
        target >>= 1
    return cnt


for target in range(0, 1 << n):
    if get_count(target) >= 2:
        answer += 1

print(answer)