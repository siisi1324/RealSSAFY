# KMP 알고리즘
# 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로,
# 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
# 시간복잡도 O(M+N)

# 이런 효율적인 방법도 있다 라는 정도의 이해가 필요

def kmp(t, p):
    N = len(t)  # 전체 문자열(텍스트)의 길이
    M = len(p)  # 찾을 패턴의 길이
    
    lps = [0] * (M+1)  # LPS(Longest Prefix Suffix) 배열 생성
    j = 0  # 현재까지 일치한 부분의 길이 (비교할 패턴 위치)
    lps[0] = -1  # 첫 번째 요소는 -1로 설정
    
    # **전처리 과정: LPS 배열을 생성**
    for i in range(1, M):
        lps[i] = j  # 이전까지 일치한 개수 저장
        if p[i] == p[j]:  # 같은 문자가 반복되면 j 증가
            j += 1
        else:
            j = 0  # 불일치하면 j 초기화
    lps[M] = j  # 마지막 LPS 값 저장
    
    # **검색 과정: KMP 알고리즘을 사용한 문자열 검색**
    i = 0  # 비교할 텍스트 위치
    j = 0  # 비교할 패턴 위치
    
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:  # 첫 글자가 불일치하거나, 문자가 일치하면
            i += 1  # 텍스트 인덱스 증가
            j += 1  # 패턴 인덱스 증가
        else:  # 불일치하면 LPS 값을 사용하여 점프
            j = lps[j]  
        
        if j == M:  # 패턴을 찾은 경우
            print(i - M, end=' ')  # 패턴이 처음 등장하는 위치 출력 (0-based index)
            j = lps[j]  # 다음 검색을 위해 j 이동
    
    print()  # 줄바꿈 (출력 형식 정리)
    return

# 테스트 데이터
t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)

t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)

t = "AAAAABAAABA"
p =  "AAAA"
kmp(t, p)

t = "AAAAABAAABA"
p =  "AA"
kmp(t, p)
