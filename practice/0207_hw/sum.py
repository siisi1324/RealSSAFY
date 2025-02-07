N = 100
 
for testcase in range(10):
    test = int(input())
    matrix = [list(map(int,input().split()))for _ in range(N)]
 
    max_v = 0
 
    sum_List = []
    for i in range(N):
        sum_r = sum_c = 0
        for j in range(N):
            sum_r += matrix[i][j]
            sum_c += matrix[j][i]
        sum_List.append(sum_r)
        sum_List.append(sum_c)
 
    sum_d1 = sum_d2 = 0
    for i in range(N):
        sum_d1 += matrix[i][i]
        sum_d2 += matrix[i][N-1-i]
 
    sum_List.append(sum_d1)
    sum_List.append(sum_d2)
 
    for item in sum_List:
        if item >= max_v:
            max_v = item
 
    print(f'#{test} {max_v}')