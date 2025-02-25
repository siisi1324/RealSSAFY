# stack을 만들기 위해서 필요한 거
# 1. 리스트 : 데이터를 저장하는 목적
# 2. top 변수 : stack의 마지막 요소를 가리키는 변수
# 3. push, pop

# 클래스로 만들어보기
class MyStack:
    #상태값 : 리스트, top
    def __init__(self,length):
        self.max_size = length
        self.s = [None] * length
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        return False
    
    def is_full(self):
        if self.top + 1 == self.max_size:
            return True
        return False

    def push(self,data):
        if not self.is_full():
            self.top += 1
            self.s[self.top] = data
        else:
            print('가득 찼는데요?')

    def pop(self):
        if not self.is_empty():
            value = self.s[self.top]
            self.top -= 1
            return  value
        return None

# 크기가 3인 스택 생성
stack = MyStack(3)

# 스택에 값 추가 (push)
stack.push(10)
stack.push(20)
stack.push(30)

# 스택이 가득 찬 상태에서 push
stack.push(40)  # "가득 찼는데요?" 출력

print('=====================================================')

# 이런식으로 해도 된다~ 할줄만 알면 된다~

stack = [None] * 100
top = -1
top += 1
stack[top] = 'A'
top += 1
stack[top] = 'B'
top += 1
stack[top] = 'C'
top += 1
stack[top] = 'D'
top += 1
stack[top] = 'E'

print(stack[top])
top -= 1
print(stack[top])
top -= 1
print(stack[top])
top -= 1
print(stack[top])
top -= 1
print(stack[top])
top -= 1
print(stack)


print('=====================================================')

# 강사님이 재귀랑 스택이 비슷해서 알려주신 예시
def my_func1():
    a = 10
    my_func2()
    print(f'my_func1 > a : {a}')
    

def my_func2():
    a = 5
    my_func3()
    print(f'my_func2 > a : {a}')
    

def my_func3():
    a = 3
    print(f'my_func3 > a : {a}')


my_func1()

# my_func3 > a : 3
# my_func2 > a : 5
# my_func1 > a : 10