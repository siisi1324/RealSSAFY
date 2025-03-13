arr = [2, 5, 2, 9, 3, 1, 8, 4]
N = len(arr)
subset = []


# 모든 부분집합의 집합 : power set(멱집합)
# 각 요소에 대해서 부분집합에 포함시키는 경우와 포함시키지 않는 경우 모두 고려
# idx번 요소를 부분집합에 포함시키는 경우, 포함시키지 않는 경우
def power_set(idx):
    if idx == N:  # 결정할 수 있는 인덱스를 벗어남
        print(subset)
        return
    # idx번 요소를 부분집합에 포함한 경우
    subset.append(arr[idx])
    power_set(idx + 1)
    # idx번 요소를 분집합에 포함하지 않은 경우
    subset.pop()
    power_set(idx + 1)


check = [0] * N


def power_set2(idx):
    if idx == N:  # 결정할 수 있는 인덱스를 벗어남
        # print(check)
        print('[', end=' ')
        sum_value = 0

        for i in range(N):
            if check[i]:
                print(arr[i], end=' ')
                sum_value += arr[i]
        print(']', sum_value, sum(check))

        return
    # idx번 요소를 부분집합에 포함한 경우
    # check[idx] = 1
    # power_set2(idx + 1)
    # # idx번 요소를 분집합에 포함하지 않은 경우
    # check[idx] = 0
    # power_set2(idx + 1)
    #
    for i in range(2):
        check[idx] = i
        power_set2(idx + 1)


power_set2(0)


