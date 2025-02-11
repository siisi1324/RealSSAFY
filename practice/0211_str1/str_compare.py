# # 혜정이언니의 만능 레시피
# def is_include(a, b):
#     list1 = arr2.split(arr1)
#     if len(list1)>=2:
#         return 1
#     else:
#         return 0



# T = int(input())
# for tc in range(1, T+1):
#     arr1 = input()
#     arr2 = input()
#     result = is_include(arr1, arr2)
#     print(f'#{tc} {result}')


print('=====================================================')

# 강사님 풀이
# 짧은단어(포함돼야할)는 계속 반복하고, 긴 문장은 옮겨가면서 비교한다. 

def solve(str1, str2):
    N = len(str2)  # 긴 문자열의 길이
    M = len(str1)  # 짧은 문자열의 길이
    
    for i in range(N - M + 1):  # i : 비교하려는 시작 인덱스
        for j in range(M):  # 검사할 인덱스
            # str1[j] 과 str2[i+j]를 비교
            if str1[j] != str2[i+j]:  # 다르면 검사 종료
                break
        else:  # break 문이 한 번도 실행되지 않으면 실행됨 (즉, 모든 글자가 일치)
            return 1
    
    return 0  # 찾지 못한 경우

T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    str1 = input().strip()  # 단어 1
    str2 = input().strip()  # 단어 2
    result = solve(str1, str2)
    print(f'#{tc} {result}')

