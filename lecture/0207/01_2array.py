# 2차원 리스트
# 1차원 리스트를 묶어놓은 리스트

# 2차원 리스트 만들기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

print('=====================================================')


# 0으로 이루어진 2차원 리스트 만들기
arr = [[0]*4 for _ in range(3)]
arr = [[[0] for _ in range(N)]for _ in range(N)]
# ( ) 말고 [ ] 쓰기
# 자주쓰니 외우기
# ([0] * 4)*4 절대안댐
# 모든 1차원 배열의 인덱스(밸류)들이 같은 밸류를 가르킨다. 

print('=====================================================')

for i in range(n):
    for j in range(m):
        f(array[i][j]) # 필요한 연산 수행
        # f 는 임의의 함수

print('=====================================================')

# 지그재그 순회
# 외울필요 전혀 없다.
for i in range(n):
    for j in range(m):
        f(array[i][j + (m-1-2*j) * (i%2)])

# 짝수일 때 : j + (m-1-2*j) * (0) → j (그대로)
# 홀수일 때 : j + (m-1-2*j) * (1) → j + (m-1-2*j) = j+m−1−2j = m−1−j (반대순서로 진행)

