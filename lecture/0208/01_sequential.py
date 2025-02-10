# 순차검색
# 일렬로 되어 있는 자료를 순서대로 검색하는 방법
# 슈도코드 <- == = (배정연산자)

# 1) 정렬되어 있지 않은 경우
# 자꾸 함수로 만들 버릇하기
def seq_search(arr, n, key):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == key:
                return 1
    return -1  # 모든 원소가 KEY보다 작으면     

arr = [[1,2,3],[4,5,6],[7,8,9]]
N = 3
key = 5

print(seq_search(arr, N, 5))

print('=====================================================')

# 2) 정렬되어 있는 경우

def seq_search(a, n, key):
    for i in range(n):
        if a[i] == key:
            return 1
        elif a[i] > key :return -1
    return -1



arr = [4, 9, 11, 23, 2, 19, 7]

arr.sort()
print(seq_search(arr, len(arr), 100))
print(seq_search(arr, len(arr), 11))


