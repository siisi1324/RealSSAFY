s = 0
for i in range(5):
    s += A[i][i]
    s += A[i][4-i]

s-=A[5//2][5//2]