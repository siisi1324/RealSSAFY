# <카운팅 정렬>
# 갱장히 빠르다..제약사항은 많다..(비교적 짧은 정수배열만 가능)


DATA = [0, 4, 1, 3, 1, 2, 4, 1] #을 카운팅 정렬하는 과정

# 리스트의 밸류들이 인덱스로 사용됨!!

COUNTS = [0] * 5 # max(data) + 1

# 1단계 : Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장한다. 
for i in range(len(DATA)): # 각 숫자의 개수 
    COUNTS[DATA[i]] += 1

# 누적합 구하기 : 누적합을 구하면 각요소가 어디에 들어가는지 계산하는 과정
for i in range(1, 5): # COUNTS[i]까지의 합계
    COUNTS[i] += COUNTS[i-1]
    # [0, 0+1, 0+1+2, 0+1+2+3, 0+1+2+3+4...] 식

TEMP = [0] * len(DATA) # 새로운 배열을 넣을 리스트 발생

for i in range(len(DATA)-1, -1, -1):
    COUNTS[DATA[i]] -= 1 # DATA[i]까지의 개수 1개 감소
    # 2단계 : 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정한다. 
    TEMP[COUNTS[DATA[i]]] = DATA[i]
    # 새로운 리스트를 완성한다. 

print('====================================================')

# <카운팅정렬 정리본>
def Counting_Sort(DATA, TEMP, k):
    # k = 아마 DATA 리스트의 최댓값
    COUNTS = [0] * (k+1)

    for i in range(len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, k+1):
        COUNTS[i] += COUNTS[i-1]

    for i in range(len(DATA)-1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]

    print(TEMP)