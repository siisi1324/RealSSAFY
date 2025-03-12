# 완전탐색 문제 2. 연속 3장의 트럼프 카드
# A, J, Q, K 네 종류의 카드들이 다량으로 쌓여져 있다.
# 이 중, 5장의 카드를 뽑아 나열하고자 한다.
# 같은 종류의 카드가 세 장 연속으로 나오는 경우의 수를 구하여라.


path = []
card = ['A', 'J', 'Q', 'K']
cnt = 0

def triplet(path):
    if path[0]==path[1]==path[2] or path[1]==path[2]==path[3] or path[2]==path[3]==path[4]:
        return 1
    else:
        return



def solve(num):
    global cnt
    if num==5:
        if triplet(path):
            cnt += 1
        return

    for i in range(4):
        path.append(card[i])
        solve(num + 1)
        path.pop()

solve(0)
print(cnt)
