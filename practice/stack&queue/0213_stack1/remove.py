# 내 코드
def solve(arr):
    stack = [None] * 100 # 일단 스택만들기
    top = -1 # top생성
    for i in arr: # 문자열(리스트) 돌기
        if i == stack[top]: # 직전의 문자와 동일한 경우
            stack.pop(top) # 삭제시키기, [], () 조심하기
            top -= 1 # top(인덱스)도 줄이기
        else: # 그 외의 경우
            top += 1 # 추가추가 
            stack[top] = i
            
        
    return top+1 # 문자열의 길이는 +1인것


T = int(input())
for tc in range(1, T+1):
    Arr = list(input()) # 문자열을 바로 리스트로 만들기, 이때부터 조심하기
    result = solve(Arr)
    print(f'#{tc} {result}')

print('=====================================================')


def check_word(txt):
    N = len(txt)        # 입력한 문자열 txt 의 길이
    check_txt = [None] * N  # 반복문자를 지운 문자를 저장할 변수
    cnt = 0             # 초기 카운터(유효 문자 개수) 0
    for i in range(N):
        check_txt[cnt] = txt[i]
        if cnt > 0 and check_txt[cnt - 1] == check_txt[cnt]: # 지금 위치와 이전 위치의 글자가 같다면
            # 반복된 같은 문자 제거.
            check_txt[cnt] = None
            check_txt[cnt-1] = None
            cnt -= 1    
        else:     # 제일 처음 시작할 때에도 아무것도 없는 상태에서 시작하니까 if문을 패스하고 cnt 값에 + 1이 된다.
            cnt += 1    # 새로운 문자이면 개수 증가
 
    return cnt
 
 
T = int(input())
for test in range(1, T+1):
    txt = input()
    result = check_word(txt)
    print(f'#{test} {result}')