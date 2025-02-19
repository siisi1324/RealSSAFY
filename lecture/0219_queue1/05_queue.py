# 링크드 큐는 알면 좋고, 몰라도 괜찮다(그림위주의 이해가 좋음)
# 연결 큐 : 노드끼리 연결된 형태의 큐
# front만 저장하고 있으면...
class Ndoe:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, data):
        # 맨 마지막 요소 찾아서 거기에 새로운 노드 달아주기
        if self.front is None:
            self.front = Node(data)
        last = self.front
        next = last.next
        while current is not None:
            last = next
            next = last.next
            current = current.next
        pass
    def dequeue(self):
        # 
        pass
