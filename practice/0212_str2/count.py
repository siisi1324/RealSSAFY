def solve(W, T):
    list_1 = [0] * len(W)
    max_num = 0
    for i in range(len(W)):
        for j in range(len(T)):
            if W[i] == T[j]:
                list_1[i] += 1
    
    for i in list_1:
        if max_num < i:
            max_num = i
    return max_num


T = int(input())
for tc in range(1, T+1):
    word = list(input())
    txt = list(input())
    result = solve(word, txt)
    print(f'#{tc} {result}')
