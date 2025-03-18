# 이전 제출에서 min_v 없이 반환을 하기 위한 코드
def recur(cnt, total):
    if total >= B:  # 재귀하는 동안 목표값(B) 보다 크거나 같다면 최소값 갱신시키기.
        return total - B

    if cnt == N:  # N명 만큼에 대하여 선택했다면 그만.
        return float('inf')

    choose = recur(cnt + 1, total + h_i[cnt])  # 포함 시키는 경우

    no_choose = recur(cnt + 1, total)  # 포함 안하는 경우

    return min(choose, no_choose)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    h_i = list(map(int, input().split()))
    result = recur(0, 0)
    print(f'#{tc} {result}')


# ======================================================================================================
# 장훈이의 높은 선반

T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    N, B = map(int, input().split())  # 점원의 수 N, 선반의 높이 B 를 입력.
    lst = list(map(int, input().split()))  # 모든 점원의 키를 입력.
    sml_height = 200001  # 직원의 키 조합 최댓값인 200001을 선반과 직원의 키 차이로 설정.

    for i in range(1 << N):  # 0 ~ 2 ** N(직원 부분집합의 수)까지의 모든 숫자를 2진수로 변환하여 부분집합을 찾음.
        height = 0  # 점원의 부분집합의 키 합산값을 구하기 위해 변수를 설정.
        for j in range(N):  # 모든 점원을 돌면서 2진수와 비교하여
            if i & (1 << j):  # 부분집합을 이루는 숫자를 찾아낸 다음
                height += lst[j]  # 키 합산값에 더해줌.
        if height < B:  # 키 합산값이 선반 높이보다 낮다면
            continue  # 넘어가고 다음 부분집합을 확인.
        elif sml_height > height - B:  # 키 합산값이 선반 높이보다 높고 두 값의 차이가 키 값 차이 최솟값보다 작다면
            sml_height = height - B  # 키 값 차이 최솟값을 갱신.

    print(f'#{tc} {sml_height}')  # 양식에 맞게 출력.