def check_babygin(arr):
    for i in range(10):
        if arr[i] >= 3:
            return True
        if arr[i] >= 1 and i < 8:
            if arr[i+1] >= 1 and arr[i+2] >= 1:
                return True


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    for i in range(12):
        if i % 2 == 0: # 홀수번째 카드라면(0부터 시작이니까)
            p1[arr[i]] += 1
            if check_babygin(p1):
                print(f'#{tc} 1')
                break
        elif i % 2 != 0:
            p2[arr[i]] += 1
            if check_babygin(p2):
                print(f'#{tc} 2')
                break
    else:
        print(f'#{tc} 0')





