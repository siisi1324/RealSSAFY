# 봤을 때, 양쪽 각각 2칸을 포함한 5칸 중에서 가장 큰 수일때, 그 다음으로 큰 수를 뺀 값들을
# 합하면 되는 식인 것 같습니다. 

for x in range (1, 11): # 10번 반복
    num = int(input()) # 길이 입력 
    list1 = list(map(int, input().split())) # 리스트 입력
    list2 = [] # 새로운 작은 배열 넣을 것
    total_num = 0 # 조망권이 있는 칸의 총합
    for i in range(2, num-2): # 0칸을 제외하고 
        list2 = list1[i-2:i+3] # 다만 5칸이 되도록
        if list2[i] == max(list2): # 중앙값이 최고값인 경우에만
            num1 = max(list2)
            num2 = 0 # 우선 중앙값을 최고값으로 입력 
            if list2[i] != num1 and max(list2): # 그리고 두번째 최고값을 찾기위해 없앤다. 
                num2 = max(list2) # 다시 두번째 최고값을 찾는다. 
            # 최고값을 없애고, 다시 두번째 최고값을 찾으려고도 해봤는데 실패
            total_num += (num1-num2) # 조망권에 넣는다. 
    print(f'#{x} {total_num}') # 조망권 출력

