# 1부터 주어진 숫자까지 더한 값을 출력하시오/

num = int(input())
sum = 0
for i in range(num+1):
    sum += i
print(sum)