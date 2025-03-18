# 1000명의 학생들의 성적 중에 가장 많이 나온 점수를 출력하세요. (점수는 0점에서 100점 사이)
# 단 여러 개의 최빈수가 있는 경우에는 가장 큰 정수를 출력하라.


import sys
sys.stdin = open("mostnum.txt", "r")

T = int(input())
for tc in range(1, T+1):
    tc = int(input())
    arr = [0] * 101
    score_arr = list(map(int, input().split()))

    for score in score_arr:
        arr[score] += 1

    most_index = 0
    most_num = arr[0]
    for i in range(len(arr)):
        if arr[i] >= most_num:
            most_num = arr[i]
            most_index = i
    print(f'#{tc} {most_index}')

