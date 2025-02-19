# 선형 큐의 단점 : 포화상태와 비어있는 상태를 제대로 판단하지 못한다. 
# 단점을 보완하기 위해서 rear와 front가 마지막 인덱스까지 갔을 때...
# 0번으로 다시 보내버리기 -> 재사용이 가능하다.
N = 10
arr = [None] * N
front = rear = -1
# 포화 상태 판단 : rear 다음 칸이 front라면 포화상태
# 비어있는 상태 : rear와 front가 같은 칸이라면 비어있는 상태

def enqueue(data):
    global rear
    if (rear + 1)%N == front:
        print('가득 찼어요')
        return
    rear = (rear+1)%N
    arr[rear] = data
    pass

def dequeue():
    global front
    if front == rear :
        print('비어있어요')
        return 
    front = (front+1)%N
    return arr[front]
