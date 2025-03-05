def heappush(data):
    global heapcount
    heapcount += 1
    heap[heapcount] = data
    current = heapcount
    parent = current//2
    while current > 1 or heap[current] < heap[parent]:
        if heap[current] < heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = current // 2
    return heap

T = int(input())
for tc in range(1, T+1):
    heap = [0] * 1000
    heapcount = 0
    N = int(input())
    arr = list(map(int, input().split()))
    for i in arr:
        heappush(i)

    sum = 0
    index_last = heapcount//2
    while index_last != 0:
        sum += heap[index_last]
        index_last //= 2

    print(f'#{tc} {sum}')


