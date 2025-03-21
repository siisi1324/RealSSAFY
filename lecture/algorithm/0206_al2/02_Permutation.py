# 0에서 9사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의
# 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.

# 222 = trilplet
# 123 = run
# 6장의 카드가 run과 triplet으로만 구성된 경우는 baby-gin


# <완전탐색>
# 완전탐색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법이다.
# Brute-force 혹은 generate-and-test 기법이라고도 불리운다.
# 모든 경우의 수를 테스트한 후, 최종 해법을 도출한다. 
# 일반적으로 경우의 수가 상대적으로 작을 때 유용하다. 
# 보통 a형까지도 완전검색 위주.. 나중엔 최적화

# 부분집합, 조합, 순열, DFS, BFS 을 알아야 한다. 


print("----------------------------------------------------------------")

# <순열>
# 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
# 서로 다른 n개 중 r개를 택하는 순열은 아래와 같이 표현한다. 
# nPr
# nPr = n * (n-1) * (n-2) * ... * (n-r+1)
# nPn = n * (n-1) * (n-2) * ... * (n-r+1) * ... * 2 * 1

# 예제) {1,2,3}을 포함하는 모든 순열을 생성하는 함수
arr = [2, 3, 7]
for i1 in range(3):
    for i2 in range(3):
        if i2 != i1:
            for i3 in range(3):
                if i3 != i1 and i3 != i2:
                    print(arr[i1], arr[i2], arr[i3])

print("----------------------------------------------------------------")

# 예제2)
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)

print("----------------------------------------------------------------")

# 예제3)
# perm 의 0번 칸에 넣을 수 있는 거 다 넣어보기
arr = [1,2,3]
N = len(arr)
perm = [0] * N

#perm 의 0번 칸에 넣을 수 있는거 다 넣어보기
for i in range(N):
    perm[0] = arr[i]
    for j in range(N):
        #j는 i와 같으면 안됨, 같아도 되는건 중복순열
        if i == j : continue
        perm[1] = arr[j]
        for k in range(N):
            if k == i or k == j : continue
            perm[2] = arr[k]
            print(perm)

