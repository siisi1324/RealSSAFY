# 혜정이언니의 만능 레시피
def is_include(a, b):
    list1 = arr2.split(arr1)
    if len(list1)>=2:
        return 1
    else:
        return 0



T = int(input())
for tc in range(1, T+1):
    arr1 = input()
    arr2 = input()
    result = is_include(arr1, arr2)
    print(f'#{tc} {result}')


print('=====================================================')
# for-else문은 파이선에서만 쓰는 문법
# 플래그변수랑 어쩌고 쓰는 법 해달라...

T = int(input())
for tc in range(1, T+1):
    str1 = input() # 단어
    str2 = input() # 단어2
    N = len(str1)  # 긴 문자열의 길이
    M = len(str2)  # 짧은 문자열의 길이
    def solve





    for i in range(N-M+1): 
        is_find = True
        for j in range(M): # 검사인덱스
            # str1[j]과 str2[i+j]를 비교
            if str1[j] != str2[i+j]:
                is_find = False
                break
    
        if is_find:
            return 1
        # 반복문 다 도는동안...다 맞으면 마ㅏㅈ다요
    return 0