# 이런것도 있구나..정도에서 만족하시고 나중에 또나온다. 지금 그래도 최대한 이해하라...

# 부분집합 
a = [2, 3, 7]
bit = [0,0,0]
for i in range(2):
    bit[0] = i                  # 0번 원소
    for j in range(2):
        bit[1] = j              # 1번 원소
        for k in range(2):
            bit[2] = k         # 2번 원소
            for b in range(3):
                if bit[b]:
                    print(a[b], end = ' ')   # 3번 원소  
            print(bit)