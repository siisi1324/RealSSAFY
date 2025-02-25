def is_plin(W):
    result = 0
    # 사실 이런거 필요없긴 하지. 맞으면 return 1 아니면 return 0하면 되니께..
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
    
print('=====================================================')

# 조경호님 코드

def solve(word):
    n = len(word) # 글자 길이
    for i in range(n//2):
        if word[i] != word[n-1-i]:
            return 0
    return 1
 
T = int(input())
for tc in range(1, T+1):
    word = input().strip()
    # solve(word)
    print(f'#{tc} {solve(word)}')