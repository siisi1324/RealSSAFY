# 패턴이나 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
T = int(input())

for tc in range(1, T+1):
    arr = input()
    for i in range(1, len(arr)):
        if arr[:i] == arr[i:i*2]:
            print(f'#{tc} {i}')
            break

