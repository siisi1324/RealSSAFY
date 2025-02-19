def solve(arr):
    stack = [None] * 100
    top = -1
    for i in arr:
        if i == stack[top]:
            stack.pop(top)
            top -= 1
        else:
            top += 1
            stack[top] = i
            
        
    return top+2





T = int(input())
for tc in range(1, T+1):
    Arr = list(input())
    result = solve(Arr)
    print(f'#{tc} {result}')