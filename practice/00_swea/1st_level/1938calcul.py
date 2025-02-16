# 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.

A, B = map(int, (input().split()))

print(f'{A+B}')
print(f'{A-B}')
print(f'{A*B}')
print(f'{A//B}')