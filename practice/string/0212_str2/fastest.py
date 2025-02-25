def solve(w1, w2):
        # 문장, 패턴
    len1 = len(w1) # 문장길이
    len2 = len(w2) # 패턴길이
    cnt = 0 # 갯수
    i = 0 # 시작점 
    while i < len1-len2+1: # 시작점 정의(반복횟수)
        for j in range(len2): # 길이만큼 맞는지 확인
            if w1[i+j] != w2[j]: # 틀리면 
                i += 1 # i위치 수동으로 1늘리기(다시 반복)
                break       
        else: 
            cnt += 1 # 패턴길이만큼 맞으면 갯수 +1
            i += len2 # i 위치는 패턴이 맞을 때 시작위치에서 끝위치로 옮기기 
    return len1-(len2*cnt)+cnt # 패턴의 길이를 1로 바꾸는 작업


T = int(input())
for tc in range(1, T+1):
    Rword, Sword = input().split()  # 문장, 패턴 정의
    result = solve(Rword, Sword)    
    print(f'#{tc} {result}')


print('=====================================================')

# 박상훈님 코드
T = int(input())  # test case
 
for tc in range(1, T + 1):  # test case 만큼 반복
 
    A, B = input().split()  # 글자를 나눠서 받음
    A = list(A)
    B = list(B)  # 각각 list 화.
 
    start = 0  # 같은 글자를 찾는 곳을 정하기 위해 변수를 설정
    count = 0  # 타이핑 횟수를 세기 위해 변수를 설정
 
    while start <= len(A) - len(B) + 1:  # 마지막에 B 길이만큼 찾고 나면 종료
 
        for i in range(len(B)):  # B 길이만큼 반복
            if A[i + start] != B[i]:  # 같은 부분이 아닐 경우
                start += 1  # 바로 옆 칸으로 넘어가고
                count += 1  # 방금 기준 삼았던 글자는 타이핑
                break
        else:  # 같은 부분이라면
            start = start + i + 1  # 통째로 넘어가 그 다음 칸을 기준으로 잡고
            count += 1  # 전체를 한 번 타이핑
 
    count += len(A) - start  # 남은 길이만큼 타이핑
    print(f'#{tc} {count}')

print('=====================================================')

# 최혜정 언니 코드

T = int(input()) # 테스트케이스 받기
for t in range(T):
    a, b= input().split()
    n = len(a) # 각 문자열 길이
    m = len(b)
    cnt = 0
    i = 0
    while i < n-m+1: # a의 시작점 세팅
        for j in range(m): # b문자열 길이만큼 반복
            if a[i+j] != b[j] : # 비교
                i += 1 # 문자열 b와 일치하지않으면 시작점 +1 이동
                break
        else : # 문자열 b와 일치하면
            i = i+m # 시작점을 b 길이만큼 이동
            cnt += 1 # cnt +1
    result = (n - cnt * m) + cnt ## b와 일치하지 않는 글자수 + b문자열의 수 = a에서 발견된 문자열을 제외한 것 - 발견된 b문자열의 수
    print(f'#{t+1} {result}')


print('=====================================================')

# 박준형님 코드
T = int(input())
for test_case in range(1, 1 + T):
    A, B = map(list, input().split())

    # A에서 숫자 하나씩 pop 해서 temp_list에 입력
    temp_list = []
    for i in range(len(A)):
        if len(A) > 0:
            temp = A.pop(0)  # pop
            temp_list.append(temp)  # temp list에 입력
        else:
            break  # A가 비었을 때 pop에러 나지않게 break

        if temp_list[-len(B)::] == B:  # append가 뒤에 추가하기에 뒷 요소와 B를 비교
            temp_list[-len(B)::] = [0]  # 일치한다면 key 1번 입력으로 인식하게 하도록 1개 요소짜리로 바꿔버림
    print(f'#{test_case} {len(temp_list)}')  # temp_list에 미리 B부분을 [0]으로 바꿔놨기에 len(temp_list)

