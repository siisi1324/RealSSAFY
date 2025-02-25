for t in range(1, 11):
    dump_n = int(input())
    list1 = list(map(int, input().split()))

    for _ in range(dump_n):
        min_v = list1[0]
        max_v = list1[0]
        Rmin = 0
        R_max = 0
    
        for i in range(len(list1)):
            if list1[i]<min_v:
                min_v=list1[i]
                Rmin = i
            if list1[i]>max_v:
                max_v=list1[i]
                R_max = i
        # 얘네는 Rmin과 R_max가 정해지고 난 후에 평탄화 작업을 해야 한다. 
        list1[Rmin] += 1
        list1[R_max] -= 1
        # min_v += 1
        # max_v -= 1
        # 이렇게 해봤자 list1에서는 바뀌지가 않는다. 
        if max_v - min_v <= 1:
            break
        # 이게 평탄화가 완료되면 넣어볼 만한 조건이다.


    # 여기서는 그냥 새로 구한다. Rmin, R_max는 의미가 없다.
    real_min = list1[0]
    real_max = list1[0]
    for i in list1:
        if real_min > i :
            real_min = i
        if real_max < i:
            real_max = i
    diff = real_max - real_min

    print(f'#{t} {diff}')