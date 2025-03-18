# 단어를 입력 받아 회문이면 1을 출력하고, 아니면 0을 출력해라.



T = int(input())
for tc in range(1, T+1):
    str = input()
    L_str = len(str)

# 양쪽의 끝에서부터 각각 체크
    for i in range(L_str//2):
# 하나라도 다르다, 0 출력
        if str[i] != str[L_str-i-1]:
            print(f'#{tc} 0')
            break
    else:
        print(f'#{tc} 1')
