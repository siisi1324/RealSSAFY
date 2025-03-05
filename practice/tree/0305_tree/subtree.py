# 부모번호를 인덱스로
# 왼쪽자식과 오른쪽 자식을 저장

T = int(input())
E, N = map(int, input().split())


left = [None] * V
right = [None] * V
left[5] = 1
right[5] = 2
left[1] = 3
left[2] = 6
right[2] = 4
print(left)
print(right)