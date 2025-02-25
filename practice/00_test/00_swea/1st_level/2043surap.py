P, K = map(int, input().split())

print(P-K+1)

print("----------------------------------------------------------------")

a, b = map(int, input().split())
count = 1
 
for test_case in range(1, a + 1):
    b += 1
    count += 1
    if a == b:
        print(count)
    else:
        continue;