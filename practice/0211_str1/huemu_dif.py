# 나의 코드
def find_hue(txt, n, m):    
    list = '' # 회문나올때 넣을 문자열
    for i in range(n):
        for j in range(n-m+1): # 회문을 확인하는 구간의 첫 글자 인덱스
            for k in range(m//2): # 회문의 길이 절반만큼 비교
                if txt[i][j+k] != txt[i][j+m-1-k]:
                    break # 비교 글자가 다르면 현재구간 중지
            else: 
                c = i  # 회문이 존재하는 열과 행을 저장
                # i행이라는건 사실 불필요.. 
                r = j
                for k in range(j, j+m): # 회문저장 길이 m만큼
                    list += str(txt[c][k])
    for i in range(n): # 행과 열만 바뀌면 동일..
        for j in range(n-m+1): 
            for k in range(m//2): 
                if txt[j+k][i] != txt[j+m-1-k][i]:
                    break 
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

print('=====================================================')

# 준기오빠코드(목강사님코드)

def solve(data):
        for i in range(N):  # i는 행번호
            for j in range(N - M + 1):  # j는 열번호 , 검사 대상 시작점
                # j번에서 시작하는  길이 M짜리 문자열 검사
                is_find = True
                for k in range(M // 2): 
                    if data[i][j + k] != data[i][j + M - 1 - k]:
                        # 회문이 아님!
                        is_find = False
                        break
                if is_find !=0 :  # j번에서 시작하는 길이 M짜리 회문 찾음!
                    result = ''
                    for a in range(j, j + M):
                        result += data[i][a]
                    return result
        return ''


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    
    palindrome = solve(data)
    if palindrome == '':  # 가로 없으니 열 검사
        trmtx = list(zip(*data))
        # list(zip(*data)) 를 하면 zip() 결과를 리스트로 변환해서 최종적으로 전치 행렬(transposed matrix) 을 만들어 줘.
        palindrome = solve(trmtx)
    print(f'#{tc + 1} {palindrome}')
    # 회문이라면 출력하고 종료
    