# <DP>

# 동적 계획 (Dynamic Programming) 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.
# 동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 
# 최종적으로 원래 주어지 입력의 문제를 해결하는 알고리즘이다.## DP의 구현 방식

# recursive 방식: fibo1()
# iterative 방식: fibo2()


def fibo1(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = 10
cnt = 0 # 호출 횟수 기록
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
# print(fibo2(n), cnt)
print(fibo2(100))


# memoization을 재귀적 구조에서 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다.
# 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.