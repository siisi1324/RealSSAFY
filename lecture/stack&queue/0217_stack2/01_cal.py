# 계산기1
# 스택으로 하니까 계산하기 쉽더라? 가 메인 아이디어
# 목표 : 높은 연산순위가 앞으로 나오는 것

# 1) 중위 표기법의 수식을 후위 표기법으로 변경한다. (스택이용)
# 2) 후위 표기법의 수식을 스택을 이용하여 계산한다. 

# in-stack-priority (스택 내부 우선순위)
# incoming-priority (스택 외부 우선순위)

# 1. 피연산자 출력
# 2. 연산자는 우선순위 높은애들 다 빼고 push





# 그리고 순열까지만 강의했다.

'''
(6+5*(2-8)/2)
6528-*2/+
'''
stack = [0]*100
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x not in '(+-*/)':   # 피연산자
        susik += x
    elif x == ')':      # '('까지 pop()
        while stack[top] != '(':    # peek
            susik += stack[top]
            top -= 1
        top -= 1        # '(' 버림. pop
    else:   # '(+-*/'
        if top==-1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
            top += 1    # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1  # push
            stack[top] = x

print(susik)

#susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*': # 피연산자면...
        top += 1            # push(x)
        stack[top] = int(x)
    else:
        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1
        if x=='+':  # op1 + op2
            top += 1                # push()
            stack[top] = op1 + op2
        elif x=='-':
            top += 1
            stack[top] = op1 - op2
        elif x=='/':
            top += 1
            stack[top] = op1 / op2
        elif x=='*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])
