# 큐
# 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
# 선입선출구조

from collections import deque # 덱

q = deque()
q.append(1)     # enqueue()
t = q.popleft() # dequeue()

list_q = []
for i in range(1000000):
    list_q.append(i)
for _ in range(1000):
    list_q.pop(0)
print('end')
# deque_q = deque()
# for i in range(1000000):
#     deque_q.append(i)
# for _ in range(1000000):
#     deque_q.popleft()
# print('end')
