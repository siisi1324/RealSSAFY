T = int(input())

for t in range(1, T+1):
    num = int(input())
    arr = list(map(int, input()))
    # input으로 받은 49679는 split()을 하지않아도 list(map(int 이 과정에서 리스트가 된다.

    # 최댓값 찾기 : 새로운 리스트를 만들어서 arr 밸류를 인덱스로 쓰기 위해서서
    maxx = arr[0]
    for i in arr:
        if maxx < i:
            maxx = i

    # 새로운 리스트 만들기
    arr2 = [0] * (maxx+1)

    # arr의 밸류들 인덱스로 써서 각각 몇개인지 쓰기
    for i in arr:
        arr2[i] += 1
        # print 하면 arr2 = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # 최댓값을 구하기 위해 arr2의 길이찾기
    lenn = 0
    for i in arr2:
        lenn += 1

    # 자 이제 마지막으로 최댓값이랑 최댓값의 밸류(개수)를 구하면댐
    most_num = arr2[0]
    most_i = 0
    for i in range(lenn):
        if arr2[i] >= most_num:
            most_num = arr2[i]
            most_i = i
        
    print(f'#{t} {most_i} {most_num}')