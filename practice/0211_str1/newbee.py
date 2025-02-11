def is_plin(W):
    result = 0
    n = len(W)
    for i in range(n//2):
        if W[i] != W[n-i-1]:
            break
    else:
        result = 1
    return result




T = int(input())
for tc in range(1, T+1):
    word = input()
    result = is_plin(word)
    print(f'#{tc} {result}')
    

