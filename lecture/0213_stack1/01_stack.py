# stack의 특성
# 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.(우리는 배열사용)

# [스택]
# 선형구조, 비선형구조가 있다.
# 후입선출 형식이다. 

# [자료구조]
# 자료를 선형으로 저장할 저장소
# 배열사용가능
# 저장소자체를 스택이라고 부르기도 한다. 
# 스택에서 마지막 삽입된 원소의 위치를 top이라고 부른다. 

# [연산]
# 삽입 : 저장소에 자료를 저장한다, 보통 push라고 부른다.
# 삭제 : 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다, pop이라고 부른다.
# isEmpty : 스택이 공백인지 아닌지를 확인하는 연산
# peek : 스택의 top에 있는 원소를 반환하는 연산


# [스택의 push 알고리즘]
# append(느려질 가능성이 있다) 메소드를 통해 리스트의 마지막에 데이터를 삽입
# (내가 만들어야 함..?)

def push(item, size):
    global top 
    top += 1
    if top == size:
        print("overflow!")
    else:
        stack[top] = item

size = 10
stack = [0]*size
top = -1

# 1번방법
push(10, size) #[10, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 2번방법
top += 1    # push(20)
stack[top] = 20

print('=====================================================')

# [스택의 pop 알고리즘]

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]
    
print(pop())

if top > -1: #pop()
    top -= 1
    print(stack[top+1])

print('=====================================================')

# [연습문제]
# 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력하세요.

top = -1
stack = [0] * 10

# push(1) 의 과정
top += 1  
stack[top] = 1

# push(2) 의 과정
top += 1  
stack[top] = 2

# push(3) 의 과정
top += 1  
stack[top] = 3

# pop
# 순서 바껴도 상관없음
# 다만 print가 아니라 return인 상황을 고려
top -= 1
print(stack[top+1])  

top -= 1
print(stack[top+1])  

top -= 1
print(stack[top+1])  