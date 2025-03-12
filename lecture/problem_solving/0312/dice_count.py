# 완전탐색 연습문제 1. 주사위 눈금의 합
# 3개의 주사위를 던져 나올 수 있는 중복 순열에 대해, 합이 10 이하가 나오는 경우는 총 몇 가지인가?


bath = []

def solve(num, sum):
    if num == 3:
        if sum <= 10:
            print(f'{bath} {sum}')
        return

    for i in range(1, 7):
        bath.append(i)
        solve(num+1, sum+i)
        bath.pop()

solve(0, 0)

#==========================================================================

bath = []
cnt = 0

def solve(num):
    global cnt
    if num == 3:
        if sum(bath) <= 10:
            cnt += 1
        return

    for i in range(1, 7):
        bath.append(i)
        solve(num+1)
        bath.pop()
    return cnt

print(solve(0))

#==========================================================================

# best way to solve problem

bath = []
cnt = 0

def solve(num, sum):
    global cnt

    if sum > 10:
        return
    if num == 3:
        cnt += 1
        return

    for i in range(1, 7):
        bath.append(i)
        solve(num+1, sum+i)
        bath.pop()

solve(0,0)
print(cnt)


