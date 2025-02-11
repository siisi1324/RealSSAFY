# 갓조경호님 코드...감사..

T = 10
for tc in range(T):
    tc_num = int(input())#testcase
    arr = [list(map(int, input().split())) for _ in range(100)] # 2차원 배열에 때려 넣기
    #[0][0] 부터 [0][100]까지 시작점을 찾아야함
    result = 0 # 결과
    for line_num in range(100):
        if arr[0][line_num] == 1: #출발점들을 찾고
            i = line_num # 현재 출발하는 위치 line_num
            for j in range(1,100):
                if i +1 <100 and arr[j][i+1] ==1: #오른쪽으로 이동이 가능하면 이동
                    while i +1 <100 and arr[j][i+1] ==1:
                        i +=1
                elif i -1 >=0 and arr[j][i-1] ==1: # 역 케이스
                    while i - 1 >= 0 and arr[j][i - 1]:
                        i -=1
            if arr[99][i] ==2 : #만약 맨 아래에서 2와 만나면 브레이크
                    result = line_num
                    break
 
 
    print(f'#{tc+1} {result}')