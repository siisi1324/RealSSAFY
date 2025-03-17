delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우


# 현재 위치 (y, x)에서 시작하여 7자리 수를 만드는 재귀함수
def recur(y, x, number):
    # 만약 7자리 수를 완성하면
    if len(number) == 7:
        result.add(number)
        return

    for d in delta:
        new_y = y + d[0]
        new_x = x + d[1]

        if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4:
            continue

        recur(new_y, new_x, number + matrix[new_y][new_x])


T = int(input())
for test in range(1, T + 1):
    matrix = [input().split() for _ in range(4)]

    result = set()  # 결과를 저장할 집합 (set 이라 중복을 제거)

    # 모든 시작점 (y, x)에 대해 재귀 함수 호출
    for y in range(4):
        for x in range(4):
            # 현재 위치의 숫자로 시작하여 재귀 호출
            recur(y, x, matrix[y][x])

    print(f'#{test} {len(result)}')