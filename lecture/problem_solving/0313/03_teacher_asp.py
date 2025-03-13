# Activity Selection Problem
# 활동의 시작시간과 종료시간이 주어질 때,
# 가장 많은 활동을 선택하면 몇 개의 활동을 선택할 수 있냐?
# 알고리즘
# 활동의 종료 시간 기준으로 오름차순 정렬
# 시작시간이 빠른 활동을 선택하면 된다.
#  단, 선택하려는 활동의 시작시간이 이전 활동의 종료시간 이후 일때,
# 5 9 6 10 8 11 1 4 3 5 1 6 5 7 3 8 2 13 12 14
data = list(map(int, input().split()))
activities = []
N = len(data)
for i in range(0, N, 2):
    # data[i] : 시작시간, data[i+1] : 종료시간
    activities.append((data[i], data[i + 1]))
print(activities)
# 종료시간 기준으로 오름차순 정렬
activities.sort(key=lambda x: x[1])
# print(activities)
selected_activities = []
prev_end = 0
for activity in activities:
    # 시작 시간이 이전 종료시간 이후라면...선택
    if activity[0] >= prev_end:
        selected_activities.append(activity)
        prev_end = activity[1]  # 종료시간 업데이트

print(selected_activities)