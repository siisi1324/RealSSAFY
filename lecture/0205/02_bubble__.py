# 정렬 
# 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값, 혹은 그 반대의 순서대로 재배열하는 것.

# 대표적인 정렬 방식의 종류
# 1) 버블 정렬
# 2) 카운팅 정렬
# 3) 선택 정렬
# 4) 퀵 정렬
# 5) 삽입 정렬
# 6) 병합 정렬

# #) 버블 정렬

# N-1 번째 패스에서 정렬이 완성된다. 

def BubbleSort(arr, N) : 	# 정렬할 List, N 원소 수
    for i in range(N-1, 0, -1) : # 범위의 끝 위치
        for j in range(i) :		# 비교할 왼쪽 원소 인덱스 (0부터 구간마지막 인덱스 -1)
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j] 

N = int(input())
arr = list(map(int, input().split()))
BubbleSort(arr, N)
print(arr)
