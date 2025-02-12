def solve(arr):
    long_len = 0



T = 10
N = 10
for tc in range(1, T+1):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))
    result = solve(arr) if solve(arr) > solve(arr2) else solve(arr2)

def bruteforce(p, t):
    N = len(t)  # 전체 문자열의 길이
    M = len(p)
    for i in range(N - M + 1):  # 텍스트의 모든 위치에서 패턴 검색 시작
        for j in range(M):  # 패턴을 하나씩 비교
            if t[i + j] != p[j]:  # 불일치하면 내부 루프 종료
                break
        # if j == M - 1 and t[i + j] == p[j]:  # 패턴 전체가 일치하면
        #     return i  # 패턴이 발견된 위치 반환
        else:
            return i
    else: # 바깥 반복문에서 break가 동작하지 않았을 때 실행 >> 패턴 못 찾음.
        return -1