# 피보나치 수열의 call tree
# memoization은 컴퓨터 프로그램을 실행할 때 이전에 계싼한 값을 메모리에 저장해서 
# 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다. 
# 동적 계획법의 핵심이 되는 기술이다. 

def fibo1(n) :
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0 :
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n = 10
cnt = 0                 # 호출 횟수 기록
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo1(n), cnt)

