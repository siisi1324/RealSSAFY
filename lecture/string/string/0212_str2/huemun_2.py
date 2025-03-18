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

# 임창목 강사님
# arr에서 가장 긴 길이의 회문을 반환하는 함수
def solve(arr):
    #M의 길이가 고정되어있다고 가정했을 때 코드부터..
    # M = 5
    max_length = 1
    for i in range(N):
        is_find = False
        for M in range(N,max_length,-1): #검사 길이 줄이는 반복문
            for j in range(N-M+1):  #검사 시작점 이동 반복문
                is_pal = True
                for k in range(M//2):
                    if arr[i][j+k] != arr[i][j+M-1-k]:
                        is_pal = False
                        break
                if is_pal:  #회문인지 확인
                    # 회문 이다
                    if max_length < M:
                        max_length = M
                    is_find = True
                    break
                #################### 열 검사 ################
                is_pal = True
                for k in range(M // 2):
                    if arr[j + k][i] != arr[j + M - 1 - k][i]:
                        is_pal = False
                        break
                if is_pal:  # 회문인지 확인
                    # 회문 이다
                    if max_length < M:
                        max_length = M
                    is_find = True
                    break
            if is_find: # 검사 회문 길이 M을 줄이는 반복문 종료
                break
    return max_length

T = 10
for _ in range(T):
    tc = input()
    N = 100
    arr = [input() for _ in range(N)]
    result = solve(arr)
    print(f'#{tc} {result}')

print('=====================================================')

# 회문 2
# 보충강사님

def finding(field):  # 모든 행의 회문을 찾아보는 함수를 제작
    len_max = 0  # 최대 길이를 찾기 위해 변수를 설정
    for row in range(100):  # 모든 행에 대해 수행
        start = 0  # 시작 지점을 설정

        for col in range(100 - start + 1):  # 모든 시작 지점으로부터 수행
            length = 0  # 열마다 회문 찾기 이전에 length 변수로 찾을 회문의 길이를 설정

            while length <= 100 - col:  # 시작지점부터 길이가 최대인 회문을 검색할 때까지 수행
                for char in range(length // 2):  # 회문 길이 절반만큼 탐색
                    if field[row][col + char] != field[row][col - char + length - 1]:  # 앞 절반과 뒷 절반이 다르면
                        break  # 탐색 종료
                else:  # 같으면 회문이므로
                    if len_max < length:
                        len_max = length  # 길이를 len_max에 반영

                length += 1  # 회문 길이를 1 늘림
        start += 1  # 시작 지점을 한 칸 옆으로 옮김
    return len_max


T = 10  # test case

for i in range(T):  # 모든 test case 에 대해 수행

    tc = input()  # test case 의 번호를 받음

    field = [list(input()) for _ in range(100)]  # 모든 행렬을 field 로 받음

    row_finding = finding(field)  # 모든 행에 대해 최대 회문 길이를 찾음
    col_finding = finding(list(zip(*field)))  # 전치행렬을 이용해 모든 열에 대해 최대 회문 길이를 찾음

    print(f'#{tc}', end=' ')
    if row_finding >= col_finding:  # 둘 중 더 큰 값을 출력.
        print(row_finding)
    else:
        print(col_finding)


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