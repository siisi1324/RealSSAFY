def find_hue(txt, n, m):    
    list = ''
    for i in range(n):
        for j in range(n-m+1): # 회문을 확인하는 구간의 첫 글자 인덱스

            for k in range(m//2): # 회문의 길이 절반만큼 비교

                if txt[i][j+k] != txt[i][j+m-1-k]:
                    break # 비교 글자가 다르면 현재구간 중지
                    

            else: 
                c = i
                r = j
                for k in range(j, j+m):
                    list += str(txt[c][k])

                

    for i in range(n):
        for j in range(n-m+1): # 회문을 확인하는 구간의 첫 글자 인덱스
            
            for k in range(m//2): # 회문의 길이 절반만큼 비교

                if txt[j+k][i] != txt[j+m-1-k][i]:
                    break # 비교 글자가 다르면 현재구간 중지

            else: 
                c = i
                r = j
                for k in range(j, j+m):
                    list += str(txt[k][c])

    return list



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    txt = [list(input()) for _ in range(N)]
    result = find_hue(txt, N, M)
    print(f'#{tc} {result}')
    