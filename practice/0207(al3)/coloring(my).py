T = int(input())
for tc in range(1, T+1):
    cnt = 0
    sq_num = int(input())
    arr_0 = [[0] * 10 for _ in range(10)]

    for c in range(sq_num):
        r1, c1, r2, c2, color = map(int, input().split())
        # arr_0 =[([0] for _ in range(10)) for _ in range(10)]
        # 튜플화 될 수 있다.
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:
                    if arr_0[i][j] == 1:
                        pass
                    elif arr_0[i][j] < 3:
                        arr_0[i][j] += color
                else:
                    if arr_0[i][j] == 2:
                        pass
                    elif arr_0[i][j] < 3:
                        arr_0[i][j] += color
    for i in range(10):
        for j in range(10):
            if arr_0[i][j] == 3:
                cnt += 1

    print(cnt)
    # 어렵다 어려워..!!!

# for r in range(r1, r2 + 1):  # 칠해지는 행의 갯수
#     for c in range(c1, c2 + 1):  # 칠해지는 열의 갯수
#         if color == 1 and field[r][c] == 0:  # 비어있을 때만 빨강(1) 칠하기
#             field[r][c] = 1
#         elif color == 2 and field[r][c] == 0:  # 비어있을 때만 파랑(2) 칠하기
#             field[r][c] = 2
#         elif (field[r][c] == 1 and color == 2) or (field[r][c] == 2 and color == 1):  
#             field[r][c] = 3  # 빨강(1) + 파랑(2) = 보라색(3)
    # gpt의 최적화

print('=====================================================')

# 이경민 코드
def solution(informations):
    ans=0
    # 0으로 채운 10 x 10 격자
    # 입력되는 색상 및 위치 정보를 읽어 2중 for 문에서 색상 코드를 더함
    # 이 때 2중 for 문(row-col)은 10x10 전체를 조사하는 것이 아닌, 입력되는 row, col임.
    # red=1, blue=2이므로 violet=3
    # [좌상단_row, 좌상단_col, 우하단_row, 우하단_col, 색상 코드]
 
    canvas=[[0]*10 for i in range(10)]
 
    for info in informations:
        r1=info[0] # 좌상단_row
        r2=info[2] # 우하단_row
        c1=info[1] # 좌상단_col
        c2=info[3] # 우하단_col
        color=info[4] # 색상 코드
 
        for row in range(r1, r2+1): # r1~r2
            for col in range(c1, c2+1): # c1~c2
                canvas[row][col]+=color # 해당 부분에 색상 코드 더하기
                if canvas[row][col]==3: # 보라색이면...
                    ans+=1 # 보라색인 칸 수 업데이트
        
                # if canvas[row][col] == 0:  # 빈 공간이라면 현재 색상 추가
                #     canvas[row][col] = color
                # elif canvas[row][col] == 1 and color == 2:  # 빨강(1) + 파랑(2) = 보라색(3)
                #     canvas[row][col] = 3
                #     ans += 1  # 보라색 개수 증가
                # elif canvas[row][col] == 2 and color == 1:  # 파랑(2) + 빨강(1) = 보라색(3)
                #     canvas[row][col] = 3
                #     ans += 1  # 보라색 개수 증가
                
                # 같은 색상의 상자가 2개 이상일 경우를 위해서..

    return ans
 
case=int(input())
for _ in range(case):
    # N: 칠할 영역 수
    N=int(input())
    color_info=[]
    for n in range(N):
        color_info.append(list(map(int, input().split())))
    print(f'#{_+1} {solution(color_info)}')


print('=====================================================')

# 박상훈 코드
# 색칠하기

T = int(input())  # 총 test case 갯수

for i in range(1, T + 1):

    N = int(input())  # 사각형으로 색칠하는 횟수
    # 0으로 이루어진 10 * 10의 종이를 생성
    field = [[0] * 10 for _ in range(10)]
    sum = 0  # 보라색의 갯수를 세기 위해 변수를 설정.

    for j in range(N):  # 매 횟수마다

        '''
        1 2 3 3 1
        3 6 6 8 1
        2 3 5 6 2
        '''

        r1, c1, r2, c2, color = list(map(int, input().split()))  # 색칠 정보
        # 빨간색 = 1, 파란색 = 2. 즉, 보라색 = 3. 1 + 2 = 3.

        '''  만약 왼쪽 위 모서리와 오른쪽 아래 모서리라고 주어지지 않은 경우
        if r1 > r2:
            r1, r2 = r2, r1
        if c1 > c2:
            c1, c2 = c2, c1
        '''

        for r in range(r1, r2 + 1):  # 칠해지는 행의 갯수
            for c in range(c1, c2 + 1):  # 칠해지는 열의 갯수

                if color == 1:  # 색 판별. 빨간색이라면~
                    if field[r][c] == 1:  # 빨간색이 칠해져 있다면 pass
                        pass
                    elif field[r][c] < 3:  # 칠해져 있지 않다면(비었거나 파랗다면) 색칠
                        field[r][c] += color

                else:  # 빨간색이 아니라면 무조건 파란색이다.
                    if field[r][c] == 2:  # 파란색이 칠해져 있다면 pass
                        pass
                    elif field[r][c] < 3:  # 칠해져 있지 않다면(비었거나 빨갛다면) 색칠
                        field[r][c] += color

    for el1 in range(10):
        for el2 in range(10):  # 10개의 행의 10개의 인수를 확인해서
            if field[el1][el2] == 3:  # 보라색이라면 sum에 1을 추가.
                sum += 1

    print(f'#{i} {sum}')
