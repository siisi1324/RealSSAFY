# 2번 
# 보물 개수 댁셔너리 생성
# 임계값 이상을 초과하는 보물 종류의 수
# count 쓰지 마세요

def analyze_treasures(treasure_list, threshold):
    treaser_dict = {}
    # setdefault사용하기??
    cnt = 0
    for i in treasure_list:
        if i not in treaser_dict:
            treaser_dict[i] = 1
        else:
            treaser_dict[i]+=1
            # 여기서도 그냥 treaser_dict[i] = 1만을 쓰게 된다면 (if, else문 없이) 
            # 초기값 딕셔너리 설정에서 에러가 뜬다. 

    for j in treaser_dict:
        if treaser_dict[j] > threshold:
            cnt += 1

    return treaser_dict, cnt

print(analyze_treasures([], 3))
# ({}, 0)

print(analyze_treasures(["pearl", "pearl", "ruby"], 2))
# ({'pearl': 2, 'ruby': 1}, 0)
#####################################################