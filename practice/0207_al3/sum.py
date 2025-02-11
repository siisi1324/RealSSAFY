# 확실히 함수를 따로 작성해서 만드는게 변수초기화 등에서 유리한 점이 많이 보인다. 

# max_sum을 하나만 잡아서 모든 행과 열들의 합(+대각선 두개) 중에 최고 큰 애를 만들어주면되지않을까??

# 조경호님 풀이
T = 10
for tc in range(T):
    tc_num = int(input())#testcase
    arr = [list(map(int, input().split())) for _ in range(100)] # 2차원 배열에 때려 넣기
    # 이제부터 row = 행 col = 열
    # 각 행의 값 중 가장 큰 것 뽑기
    max_sum_col = 0 # 가장 큰 열을 뽑기 위해서
    max_sum_row = 0 # 가장 큰 행을 뽑기 위해서
    sum_left_diagonal = 0 # 왼쪽대각선
    sum_right_diagonal = 0 # 오른쪽 대각선
    for i in range(100):
        sum_col = 0 # 열합 초기화
        sum_row = 0 # 행합 초기화
        for j in range(100):
            sum_col += arr[i][j] # 열 더하기
            sum_row += arr[j][i] # 행 더하기
        if sum_row > max_sum_row: # 큰 값으로 교체
            max_sum_row = sum_row
        if sum_col > max_sum_col:
            max_sum_col = sum_col
        sum_left_diagonal += arr[i][i] # 왼쪽 대각선은 [0,0][1,1][2,2]
        sum_right_diagonal += arr[i][99-i] # 오른쪽 대각선은 [0,99][1,98][2,98]
    result_lst =[sum_left_diagonal, sum_right_diagonal, max_sum_col, max_sum_row]
    largest_num =0
    for num in result_lst:
        if largest_num < num:
            largest_num = num
    print(f'#{tc+1} {largest_num}')


print('=====================================================')

# 여기선 리스트로 묶어버리기~
N = 100
 
for testcase in range(10):
    test = int(input())
    matrix = [list(map(int,input().split()))for _ in range(N)]
 
    max_v = 0
 
    sum_List = []
    for i in range(N):
        sum_r = sum_c = 0
        for j in range(N):
            sum_r += matrix[i][j]
            sum_c += matrix[j][i]
        sum_List.append(sum_r)
        sum_List.append(sum_c)
 
    sum_d1 = sum_d2 = 0
    for i in range(N):
        sum_d1 += matrix[i][i]
        sum_d2 += matrix[i][N-1-i]
 
    sum_List.append(sum_d1)
    sum_List.append(sum_d2)
 
    for item in sum_List:
        if item >= max_v:
            max_v = item
 
    print(f'#{test} {max_v}')

print('=====================================================')

# 강사님코드
# arr을 순회하면서 행, 열, 대각선의 합 중 최대값을 반환하는 함수
def solve(arr):
    max_sum = -0xffffffff
    # 행 우선 순회
    for i in range(100):
        row_sum = 0
        for j in range(100):    # i행 하나를 순회하는 반복문
            row_sum += arr[i][j]    # i행 요소들 하나씩 더해주기
        if row_sum > max_sum:   #방금 구한 행의 합이 기존 최대값 보다 크면 교체
            max_sum = row_sum
    # 열 우선 순회
    for i in range(100):
        col_sum = 0
        for j in range(100):  # i열 하나를 순회하는 반복문
            col_sum += arr[j][i]  # i열 요소들 하나씩 더해주기
        if col_sum > max_sum:  # 방금 구한 행의 합이 기존 최대값 보다 크면 교체
            max_sum = col_sum

    # 대각선 합(행우선 순회 하면서 조건에 맞는 애들끼리 더 해주기)
    dia_sum_1 = 0   #우하향 i == j
    dia_sum_2 = 0   #우i상향  + j == N - 1
    for i in range(100):
        for j in range(100):
            if i == j:
                dia_sum_1 += arr[i][j]
            elif i + j == 99:
                dia_sum_2 += arr[i][j]

    max_sum = dia_sum_1 if dia_sum_1 > max_sum else max_sum
    max_sum = dia_sum_2 if dia_sum_2 > max_sum else max_sum
    return max_sum

T = 10
for _ in range(T):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = solve(arr)
    print(f'#{tc} {result}')
