# 내꺼뭔가수상...뭔가 안된다.
def solve(arr, l, n):    
    cnt = 0
    for i in range(n):
        for j in range(n-l+1):
            for k in range(l//2):
                if arr[i][j+k] != arr[i][j+(l-1)-k]:
                    break
            else:
                cnt += 1
    return cnt
            

T = 10
for tc in range(1, T+1):
    input()
    n = 100
    arr = [list(input().strip()) for _ in range(n)] 
    arr2 = list(map(list, zip(*arr))) 
    # 외우기
    # result = solve(arr) if solve(arr) > solve(arr2) else solve(arr2)
    # print(f'#{tc} {result}')
    result = 0
    for l in range(100,0,-1) :
        if solve(arr, l, n) or solve(arr2,l, n) :
            result = l
            break
    print(f'#{tc} {result}')

print('=====================================================')

# 이경민 코드
def solution(str):
    length=3
 
    while thereispalindrome(str, length):
        length+=1
 
    return length-1
 
# 배열에서 회문 찾기
def thereispalindrome(str, length):
    mini_str=''
    for i in range(100):
        for j in range(0, 100-length+1):
            for k in range(length):
                mini_str += str[i][j + k]
 
            if ispalindrome(mini_str):
                return True
 
            mini_str=''
    else: False
 
    for i in range(100):
        for j in range(0, 100-length+1):
            for k in range(length):
                mini_str += str[j+k][i]
 
            if ispalindrome(mini_str):
                return True
 
            mini_str = ''
    else: False
 
# 회문 검사 함수
def ispalindrome(str):
    for i in range(len(str)//2):
        if str[i]==str[-1-i]:
            continue
        else:
            break
    else:
        return True
 
for _ in range(10):
    case=input()
    str=[list(input()) for _ in range(100)]
    print(f'#{case} {solution(str)}')


print('=====================================================')

# 정보균 코드
# 100개를 돌리면서 그 안에서 최댓값을 찾는 직관적인 코드입니다. 
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    m_len = 0
    for M in range(1,101):
        for i in range(N):
            for j in range(N-M+1):
                sub_arr = arr[i][j:j+M]
                if sub_arr == sub_arr[::-1]:
                    if len(sub_arr) > m_len:
                        m_len = len(sub_arr)
 
    for M in range(1, 101):
        for i in range(N-M+1):
            for j in range(N):
                sub_arr = [arr[k][j] for k in range(i, i+M)]
                if sub_arr == sub_arr[::-1]:
                    if len(sub_arr) > m_len:
                        m_len = len(sub_arr)
    print(f'#{tc} {m_len}')


print('=====================================================')

# 최혜정 언니
# 100부터 1까지 길이의 회문이 매 행과열에 존재하는지 여부를 판단해서 있다고 하자마자 바로 출력
def check(data, N) :
    cnt = 0
    for i in range(100):  # 한 줄씩 체크
        for j in range(100 - N + 1):
            for k in range(N // 2):
                if data[i][j + k] != data[i][j + N - 1 - k]:
                    break
            else:
                cnt += 1
    return cnt

for tc in range(10) :
    T = int(input())
    data=[]
    for n in range(100) :
        lst = list(input().strip())
        data.append(lst)

    new_data = [list(x) for x in zip(*data)]

    result = ''
    for l in range(100,0,-1) :
        if check(data,l) != 0 or check(new_data,l) != 0 :
            result = l
            break

    print(f'#{T} {result}')