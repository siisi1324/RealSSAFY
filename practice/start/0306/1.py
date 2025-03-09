import sys
sys.stdin = open("input.txt", "r")

code_dict = {
(3, 2, 1, 1) : 0,
(2, 2, 2, 1) : 1,
(2, 1, 2, 2) : 2,
(1, 4, 1, 1) : 3,
(1, 1, 3, 2) : 4,
(1, 2, 3, 1) : 5,
(1, 1, 1, 4) : 6,
(1, 3, 1, 2) : 7,
(1, 2, 1, 3) : 8,
(3, 1, 1, 2) : 9,
}
T = int(input())
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
for i in range(N):
    for j in range(M-1, 54, -1):
        if arr[i][j] == 1:
            data = []
            for _ in range(8):
                c1, c2, c3, c4 = 0, 0, 0, 0
                while arr[i][j] == 1:
                    c4 += 1
                    j -= 1
                while arr[i][j] == 0:
                    c3 += 1
                    j -= 1
                while arr[i][j] == 1:
                    c2 += 1
                    j -= 1
                c1 = 7 - c4 - c2 - c3
                j -= c1
                data.append(code_dict[(c1, c2, c3, c4)])
            odd_sum = data[1] + data[3] + data[5] + data[7]
            even_sum = data[0] + data[2] + data[4] + data[6]
            if (odd_sum*3 + even_sum)  % 10 == 0:
                print(odd_sum + even_sum)
            else:
                print('False')



