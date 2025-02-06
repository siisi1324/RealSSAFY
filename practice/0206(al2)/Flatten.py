for t in range(10):
    dump_n = int(input())
    list1 = list(map(int, input().split()))

    min_v = list1[0]
    max_v = list1[0]

    for j in range(dump_n):
        for i in list1:
            if i<min_v:
                min_v=i
            if i>max_v:
                max_v=i
        min_v += 1
        max_v -= 1

    print(f'#{t} {max_v-min_v}')