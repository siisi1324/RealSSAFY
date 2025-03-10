T = int(input())
P, A, B = map(int, input().split())


def find_cnt(p, num):
    cnt = 0
    standard = int((1+p)/2)
    while standard != num:
        cnt += 1
        if int((1+p)/2) < P:
            cnt += 1
            l_p = int((1+p)/2)
        elif int((1+p)/2) == P:
            cnt += 1
        else:
            cnt += 1
            r_p = int((1+p)/2)
    return cnt

A_cnt = find_cnt(P, A)
B_cnt = find_cnt(P, B)