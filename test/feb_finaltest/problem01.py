# 1번,
# 1. 7일간 좋아요 평균 수(실수)
# 2. 가장 많은 좋아요 수와 가장 적은 좋아요 수의 차이(정수)
# sum, len, min, max, sorted, sort 쓰지 마시오

def analyze_likes(weekly_like_list):
    num = 0
    min_var = weekly_like_list[0]
    max_var = weekly_like_list[0]
    for i in weekly_like_list:
        num += i
        if i < min_var:
            min_var = i
        if i > max_var:
            max_var = i
    diff_num = max_var - min_var
    avg_var = num / 7
    return avg_var, diff_num

print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)

#####################################################
