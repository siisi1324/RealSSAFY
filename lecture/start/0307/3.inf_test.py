import sys

# 최대값과 최소값
max_float = sys.float_info.max  # 최대값
min_float = sys.float_info.min  # 최소값 (가장 작은 양수)

# 부호 반전이 가능한 최소값
min_neg_float = -sys.float_info.max  # 부호 반전된 최대값

# 출력
print("최대 실수값:", max_float)
# 1.7976931348623157e+308
# 1.7976931348623157 × 10^308 을 나타냄
print("최소 실수값:", min_float)
# 2.2250738585072014e-308
# 2.2250738585072014 * 10^(-308)
print("가장 작은 부호 반전 가능한 실수값:", min_neg_float)