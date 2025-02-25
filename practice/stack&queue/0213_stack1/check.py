def solve(rword):
    arr = [None] * 1000
    top = -1
    ans = 1
    pair_dict = { ')' : '(' , '}' : '{' }
    for i in rword:
        if i in '{(':
            top += 1
            arr[top] = i
        elif i in ')}':
            if top == -1:
                ans = 0
                break
            # 그냥 top -= 1을 함으로써 다음 push가 오면 덮어씌우는 방식으로 작동한다. 
            elif arr[top] != pair_dict[i]:
                ans = 0
                break
            else:
                top -= 1
            

    if top > -1:
        ans = 0
        
    return ans

T = int(input())
for tc in range(1, T+1):
    Rword = input()  # 문장, 패턴 정의
    result = solve(Rword)    
    print(f'#{tc} {result}')


