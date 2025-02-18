# 백트래킹 >> 완전탐색 하면서 가능성 없는 거 안하기
# 부분 집합중에 합이 10인 부분집합을 출력해라 라는 문제를 가정
# 순열과 부분집합은 자주 쓰이니까 익혀놓도록...

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M = 10
N = len(arr)
check = [0] * N # 요소가 1이면 idx번째 요소는 부분집합에 포함

def powerset(idx, tmp_sum):
    if tmp_sum > M : 
        return
    # 이 두줄이 가지치기다. 
    if idx == N :
        if tmp_sum == M :
            print(check)
            for i in range(N):
                if check[i]:
                    print(arr[i], end=',')
            print()
        print(check)
        return
    # 특정 상황에서 모든 경우의 수 수행해보기


    check[idx] = 1
    powerset(idx+1, tmp_sum+arr[idx]) 
    check[idx] = 0
    powerset(idx+1, tmp_sum) 

powerset(0,0)

# idx : 요소의 idx
# 요소가 부분집합에 포함되는지 안되는지 결정하는 함수


def powerset(idx):
    pass