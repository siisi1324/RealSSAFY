import math

# 공의 좌표 (x, y)
balls = [
    [0, 0],       # 힐공 (cue ball)
    [-10, -17]  # 목표구 (target ball)
]

# 차이 계산
diff_x = balls[1][0] - balls[0][0]  # 목표구 x좌표 - 힐공 x좌표
diff_y = balls[1][1] - balls[0][1]  # 목표구 y좌표 - 힐공 y좌표

# atan2를 통해 각도를 구하고 degree로 변환
angle = math.degrees(math.atan2(diff_y, diff_x))

# 결과 출력
print("각도:", angle)