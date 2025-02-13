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