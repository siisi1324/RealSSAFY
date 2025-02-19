# 피보나치

# N = 10
# arr = [0] * N

# # arr의 요소에 1,5까지 숫자 넣기
# # * 함수가 한번 호출 되어서 수행하는 작업을 명확하게!!
# def my_func(idx,num):
#     if idx == N:
#         return
#     arr[idx] = num
#     my_func(idx+1,num+10)


# my_func(0,10)
# print(arr) #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



print('=====================================================')

N = 3
arr = [0] * N

def my_func2(idx):
    if idx == N:
        print(arr)
        return
    arr[idx] = 0
    my_func2(idx + 1)
    arr[idx] = 1
    my_func2(idx + 1)

my_func2(0)


print('=====================================================')



#큰 문제를 해결하기 위해 작은 문제를 해결하는 형태
# 피보나치 수열 : f(n) = f(n-1) + f(n-2)
def fibo(n):    # 피보나치 수열에서 n번째 항을 반환하는 함수
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)
fibo(4)


