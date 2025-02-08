# 가장 큰 값을 가지는 행과 열(가장 작은 값)을 반환하기
# input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    max_num = matrix[0][0]
    col1 = 0
    row1 = 0
    len_col = 0
    for i in matrix:
        len_col += 1
        for j in i:
            if j > max_num:
                max_num = j
    
    for col in range(len_col):
        for row in range(int(len_col)):
            if matrix[col][row]==max_num:
                col1 = col
                row1 = row
                break
    
    return [col1, row1]

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]

print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
