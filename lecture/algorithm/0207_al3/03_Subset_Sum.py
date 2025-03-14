# <부분집합> 
# 부분집합을 0과 1로 계산해서 출력해내는 방법
# 모든 부분집합의 집합 >> power_set(멱집합(모든 부분집합을 담아낸 집합))
a = [2, 3, 7]
bit = [0,0,0]
for i in range(2):
    bit[0] = i                  # 0번 원소
    for j in range(2):
        bit[1] = j              # 1번 원소
        for k in range(2):
            bit[2] = k          # 2번 원소
            for b in range(3):
                if bit[b]!=0:   # 3번 원소  
                    print(a[b], end = ' ')   
            print(bit)

# [0, 0, 0]
# 7 [0, 0, 1]
# 3 [0, 1, 0]
# 3 7 [0, 1, 1]
# 2 [1, 0, 0]
# 2 7 [1, 0, 1]
# 2 3 [1, 1, 0]
# 2 3 7 [1, 1, 1]

print('=====================================================')

# 난 여기서 0인 경우를 빼고 싶었다.
# 그래서 b for문에서 0인경우를 빼는 조건을 걸어보았지만 실패.
# 여기서는 결국 총합이 0일 때를 따로 구해서 제외시켜야 한다. 

a = [2, 3, 7]
bit = [0, 0, 0]

for i in range(2):
    bit[0] = i  # 0번 원소
    for j in range(2):
        bit[1] = j  # 1번 원소
        for k in range(2):
            bit[2] = k  # 2번 원소

            # 모든 요소가 0인지 확인
            if sum(bit) == 0:
                continue  # 모든 요소가 0이면 출력 안 함
            
            for b in range(3):
                if bit[b] != 0:
                    print(a[b], end=' ')
            print(bit)  # bit 상태 출력

# 이런것도 있구나..정도에서 만족하시고 나중에 또나온다. 지금 그래도 최대한 이해하라...
# 알고리즘 문제의 기본 >>>
# 완전탐색 : 배열 순회, 순열, 조합, 집합...