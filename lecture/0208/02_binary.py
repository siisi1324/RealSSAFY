# 이진검색
# 잘 이해해야한다. 
# 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
# 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다. *****

# 1) 자료의 중앙에 있는 원소를 고른다.
# 2) 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
# 3) 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고,
# 4) 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
# 5) 찾고자 하는 값을 찾을 때까지 1~3 의 과정을 반복한다.

# 중앙값이 계속 바뀐다...!
# 짝수개일 때는 중간값 -1 +1 마음대로 한다. (정확한 중간이 중요한 것이 아님)



def binary_search(a, n, key):
    start = 0 # 검색 구간 설정
    end = n-1
    while start <= end: # 검색 구간에 1개 이상의 원소가 있으면 검색
        middle = (start + end) // 2 # 기준 위치 계산
        if a[middle] == key: # 검색성공
            return middle
        elif a[middle] > key: # 키보다 크면 왼쪽 구간 선택
            end = middle - 1
        else: # a[middle] < key, 키보다 작으면 오른쪽 구간 선택
            start = middle + 1
    return -1 # 검색구간이 남아있지 않으면, 검색 실패(찾는 값 없음)


arr = [2, 4, 7, 9, 11, 19, 23] # 오름차순 정렬된 배열열
print(binary_search(arr, len(arr), 19))
print(binary_search(arr, len(arr), 100))
print(binary_search(arr, len(arr), 1))


print('=====================================================')
 

# 인덱스 
# 데이터베이스 인덱스는 이진 탐색 트리 구조로 되어있다. 
# (별로 중요치 않은 내용인듯)

