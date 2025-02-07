arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # 원소의 개수수

for i in range(1<<n):  # 1<<n : 부분 집합의 개수수
    for j in range(n): # 원소의 수많큼 비트를 비교함함
        if i & (1<<j): # i의 j번 비트가 1인경우
            print(arr[j], end="") # j번 원소 출력
    print()
print()