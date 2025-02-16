# 입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

num = int(input())

for i in range(1, num+1):
    if (num%i) == 0:
        print(f'{i}', end=' ')