# 텍스트 파일로 부터 입력 읽어오기
# input() >>> (표준입력으로부터) 한 줄 읽어오기
# 표준 입력을 터미널이 아니라 파일입력으로 변경

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output_ladder1.txt', 'w')


# 목적지(2)에 도달하는 시작 x를 반환하는 함수수
def solve():
    # 상 : 0, 좌 : 1, 우 : 2
    d = 0 # 시작방향은 위쪽 
    dr = [-1, 0, 0]
    dc = [0, -1, 1]

    # 현재 위치
    r = 99
    c = -1
    # 시작점(c) 찾기
    for i in range(100):
        if ladder[r][i] == 2:
            c = i
            break
    
    # 움직이기 시작하기
    while True:
        if r == 0: # 맨 윗줄로 올라옴(목적지 도달함)
            break
        # 현재 위쪽으로 올라가고 있으면 양옆 확인하기
        if d == 0:
            # (r, c) : 현재위치
            if c>0 and ladder[r][c-1] != 0: # 왼쪽으로 가는길이 있으면 방향전환
                d = 1
            elif c < 99 and ladder[r][c+1] == 1: # 오른쪽으로 가는 길이 있으면 오른쪽으로 방향전환
                d = 2
        else: # 현재 왼쪽 또는 오른쪽으로 이동하고 있는 경우
            # 위쪽으로 가는길이 있는지 확인
            if ladder[r-1][c] == 1:
                d = 0
        
             
        # 한 칸 이동
        r += dr[d]
        c += dc[d]
    
    # 반복문이 끝났을 때 
    return c
            

def solve2(): 
    r = 99
    c = -1
    for i in range(100):
        if ladder[r][c] == 2:
            c = i
            break
    while True: # r의 좌표를 1씩 줄이는 반복문
        if r == 0:
            break
        # 줄이기 전에 양옆에 갈 수 있는 길이 있으면 끝까지 가기
        if c>0 and ladder[r][c-1]:
            while c>0 and ladder[r][c-1] == 1:
                c -= 1
        elif c < 99 and ladder[r][c+1] == 1:
            # 무조건 elif로 걸기
            while c < 99 and ladder[r][c+1] == 1:
                c += 1
        
        r -= 1
    return c





T = 10
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    result = solve()
    print(f'#{tc} {result}')

