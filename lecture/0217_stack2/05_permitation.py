# 순열
arr = ['a', 'b', 'c']
N = len(arr)
perm = [None] * N
# perm의 idx번째에 모든 요소 넣어보기
used = [0] * N # 0은 사용 안 한 거 1은 사용 한 거



def permutation(idx):
    if idx == N:
        print(perm)
        return
    for i in range(N):
        if not used[i]: # 요 부분이 백트래킹
            perm[idx] = arr[i]
            used[i] = 1
            permutation(idx+1)
            used[i] = 0

permutation(0)