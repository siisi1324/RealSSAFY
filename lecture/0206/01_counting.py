# <카운팅 정렬>
# 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
# but 제약 : 정수로 표현할 수 있는 자료에 대해서만 적용이 가능하다. 
# 갱장히 빠르다..제약사항은 많다..


DATA = [0, 4, 1, 3, 1, 2, 4, 1] #을 카운팅 정렬하는 과정
# 1단계 : Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장한다. 
# 2단계 : 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정한다. 



# 리스트의 밸류들이 인덱스로 사용됨!!
# 맞네 그냥 밸류자체가 인덱스니까 순서대로, 개수만큼 숫자써주기만 하면 된다.
COUNTS = [0] * 5 # max(data) + 1
N = len(DATA)

for i in range(N): # 각 숫자의 개수 
    COUNTS[DATA[i]] += 1

print(COUNTS)

# 누적합 구하기 : 누적합을 구하면 각요소가 어디에 들어가는지 계산하는 과정
for i in range(1, 5): # COUNTS[i]까지의 합계
    COUNTS[i] += COUNTS[i-1]

print(COUNTS)
for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1 # DATA[i]까지의 개수 1개 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i]

# data =[0,4,1,3,1,2,4,1]
# k = 4
# temp=[0] * len(data)
# counts = [0] * (k+1)

# for i in range(len(data)):
#     counts[data[i]] += 1

# for i in range(1,k+1) :
#     counts[i] += counts[i-1] # 누적
# print(counts)

# for i in range(len(data)-1,-1,-1):
#     counts[data[i]] -= 1
#     temp[counts[data[i]]] = data[i]

# print(temp)


def Counting_Sort(DATA, TEMP, k):
    # D
    COUNTS = [0] * (k+1)

    for i in range(len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, k+1):
        COUNTS[i] += COUNTS[i-1]

    for i in range(len(DATA)-1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]