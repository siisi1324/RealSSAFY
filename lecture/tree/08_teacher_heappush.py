# 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조

# 힙 삽입해보기
# 완전한 구현은 못해도 된다, 이해위주로 하기

# heap의 특징 :
# 1. 부모노드가 자식노드보다 항상 크다((혹은 항상 작다)
# 2. 완전이진트리를 유지해야 한다. 1번부터 번호 매길때... 빈번호가 없음

heap = [0] * 10
heapcount = 0 # heap의 마지막 요소를 가리키는 변수

def heappush(data):
    global  heapcount
    # 1. 완전 이진트리의 마지막에 요소 추가
    # 2. 부모요소랑 값비교 하면서 자리바꿔주기 * 반복
    #   (루트 또는 부모가 더 클 때까지)
    heapcount += 1
    heap[heapcount] = data
    current = heapcount
    parent = current//2
    while True:
        if current == 1 or heap[current] < heap[parent]:
            break
        if heap[current] > heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = current // 2
        # 바꿔줬으면 다시 값 변경

heappush(2)
print(heap) #[0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
heappush(5)
print(heap) #[0, 5, 2, 0, 0, 0, 0, 0, 0, 0]
heappush(7)
print(heap) #[0, 7, 2, 5, 0, 0, 0, 0, 0, 0]
heappush(10)
print(heap) #[0, 10, 7, 5, 2, 0, 0, 0, 0, 0]




# heappop
# 1. 루트 반환 및 삭제
# 2. 마지막 요소를 루트에 올리기
# 3. 자식들 중 큰 값이랑 비교해서 작으면 바꾸기(내가 더 크거나 혹은 내가 단말 노드라면 중지)


heap = [0] * 10
heapcount = 0 # heap의 마지막 요소를 가리키는 변수


def heappop():
    global heapcount
    result = heap[1]  # 기존 루트 저장
    heap[1] = heap[heapcount] # 마지막 요소 루트에 넣기
    heapcount -= 1
    # heap 모양 만들어주기
    # 자식들 중 큰거랑 바꾸기..
    current = 1
    child = current * 2
    while True:
        if child > heapcount:  # 자식이 없으면
            break
        if (child + 1) <= heapcount: #오른쪽 자식이 있으면...
            if heap[child+1] > heap[child]: # 오른쪽이 더 크면...
                child += 1 # 오른쪽 자식 위치를 선택
        if heap[child] > heap[current]:
            heap[child], heap[current] = heap[current] , heap[child]

        current = child
        child = current * 2
        
    return result # 결과값 출력을 달아줘야해요

print(heappop())
print(heap)
print(heappop())
print(heap)
print(heappop())
print(heap)
print(heappop())
print(heap)
print(heappop())
print(heap)