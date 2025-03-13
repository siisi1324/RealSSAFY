# 조합 : 집합에서 원하는 개수만큼의 요소를 뽑기
def comb(idx, cnt):
    if cnt == K:  # 원하는 개수만큼 선택함
        print(check)
        return
    # 원하는 개수만큼 요소를 선택하지 못한상태
    if idx == N:  # 모든요소에 대해서 포함여부 결정완료
        return

    check[idx] = 1  # idx번째 요소를 조합에 포함
    comb(idx + 1, cnt + 1)
    check[idx] = 0  # idx번째 요소를 조합에 포함시키지 않음!
    comb(idx + 1, cnt)


arr = [1, 2, 3, 4, 5]
N = len(arr)
K = 3
check = [0] * N

comb(0, 0)
