def solve(txt, n):    
    cnt = 0
    for i in range(8):
        for j in range(8-n+1): # 회문을 확인하는 구간의 첫 글자 인덱스
            for k in range(n//2): # 회문의 길이 절반만큼 비교
                if txt[i][j+k] != txt[i][j+n-1-k]:
                    break # 비교 글자가 다르면 현재구간 중지
            else: 
                cnt+=1
    return cnt

T = 10
for tc in range(1, T+1):
    num = int(input())
    txt = [list(input()) for _ in range(8)]
    txt2 = list(zip(*txt))
    # list(zip(*data)) 를 하면 zip() 결과를 리스트로 변환해서 최종적으로 전치 행렬(transposed matrix)을 만듦.
    result = solve(txt, num) + solve(txt2, num)
    print(f'#{tc} {result}')

print('=====================================================')

def tip(txt, n):    
    cnt = 0
    # 여기 안에다가 코드짜면 됩니다. 
    return cnt