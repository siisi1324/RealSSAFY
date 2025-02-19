# 큐 생성
queue = [0] * 3
front = rear = -1

# 1, 2, 3 인큐
rear += 1     # enqueue 1
queue[rear] = 1

rear += 1     # enqueue 2
queue[rear] = 2

rear += 1     # enqueue 3
queue[rear] = 3


while front != rear:
    front += 1    # dequeue
    print(queue[front])




front += 1
print(queue[front])

front += 1
print(queue[front])