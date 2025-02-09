T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
 
    for _ in range(N):
        sq = list(map(int,input().split()))
        a = sq[0]
        b = sq[1]
        c = sq[2]
        d = sq[3]
 
        for i in range(a,c+1):
            for j in range(b,d+1):
                arr[i][j] += 1
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2 :
                cnt +=1
 
    print(f'#{test_case} {cnt}')