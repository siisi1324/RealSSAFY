# < 함수호출 : Function call >
# 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀(후입선출)
# (함수 호출이 발생하면 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를
# 스택프레임에 저장하여 시스템 스택에 삽입)

# <Recursive call>
# 필요한 함수가 자신과 같은 경우 자신을 다시 호출하는 구조

# [재귀호출 예시]
def f(i, N):    # i 배열 인덱스, N : 배열크기
    if i==N:    # 중단조건
        return
    else:       # 재귀호출
        print(arr[i])
        f(i+1, N)


arr = [1,2,3]
f(0, 3)


print('=====================================================')

# [배열에 v가 있으면 인덱스번호, 없으면 0을 리턴]
def f(i, N, V): # i 배열 인덱스, N 배열크기, V 찾는 값
    if i==N:    # V가 없는 경우  (배열을 벗어남)
        return 0
    elif A[i] == V: # 찾은 경우
        return i
    else:  # 재귀호출
        return f(i+1, N, V)

N = 3
A = [3, 7, 6]
V = 6

print(f(0, N, V))
