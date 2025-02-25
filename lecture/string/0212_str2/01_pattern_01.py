# <패턴 매칭>
# 1) <고지식한 알고리즘> (Brute-force Algorithm)
# 얘만 잘해도 된다. 
# while과 for은 완전히 대치가능하지는 않다.(특히 인덱스 부분에서)

# 패턴이 처음 등장한 위치 출력
def bruteforce(p, t):
    N = len(t)  # 전체 문자열의 길이
    M = len(p)  # 패턴의 길이

    i = j = 0  # i: 처음 검사하는 위치

    # 패턴 검색 시작
    while i < N and j < M:  
        if t[i] != p[j]:  
            i = i - j + 1  # i와 j가 달랐던 위치 다음부터 비교시작.
            j = 0  # 패턴은 처음부터 비교시작
        else:  
            # 현재 문자가 같다면, 다음 문자 비교를 위해 i, j 모두 증가
            i += 1
            j += 1  

    # 패턴이 끝까지 일치했으면 (j가 패턴 길이 M과 같다면) 패턴이 발견된 위치 출력
    if j == M:
        return(i - j)  # 패턴이 처음 등장한 위치 출력 (0-based index)
    # i는 긴 문자열의 패턴이 존재하는 끝 인덱스에 위치할 것이다. 
    # j는 끝까지 갔으니 패턴의 길이..
    else:
        return -1


t = 'TTTTTATTAATA'  # 전체 문자열 (텍스트)!
p = 'TTA'           # 찾고 싶은 패턴

print(bruteforce(p, t))



print('===============================================================')



# 고지식한 알고리즘을 for문으로 바꾸기
for i in range(N - M + 1):
    # i번에서 시작하는 길이 M짜리 문자열 검사하기
    for j in range( M ):
        # p[j]  <----> t[i+j]
        # 같으면 진행, 다르면 종료
        if p[j] != t[i+j]:
            break
    # break가 안걸리면 실행되는 코드
    else:   # 패턴과 다른요소가 없었다! >> 패턴 찾음!
        print('패턴 찾음!')
        break
else:   # 바깥 반복문에서 break가 동작하지 않았을 때 실행 >> 패턴 못찾음!
    print('패턴 없음!')



print('===============================================================')



# 패턴의 등장 횟수 리턴
def pattern_count(p, t):    
    N = len(t)  
    M = len(p)  
    i = j = 0  
    cnt = 0  # 패턴이 등장한 횟수를 저장할 변수

    while i < N and j < M: 
        if t[i] != p[j]:  
            i = i - j + 1  # 비교했던 위치 다음 문자로 이동 
            j = 0  # 패턴 인덱스 초기화
        else:  # 현재 문자가 같다면
            i += 1  # 텍스트 인덱스 증가 (다음 문자 비교)
            j += 1  # 패턴 인덱스 증가
        
        if j == M:  # 패턴을 찾은 경우 (j가 패턴 길이 M에 도달했을 때)
            cnt += 1  # 패턴 등장 횟수 증가
            i = i - j + 1  # 다음 위치에서 다시 탐색 시작
            j = 0 
    
    return cnt  # 최종 패턴 등장 횟수 반환




t = 'TTTTTATTAATA'
p = 'TTA'
print(bruteforce(p, t))
print(pattern_count(p, t))