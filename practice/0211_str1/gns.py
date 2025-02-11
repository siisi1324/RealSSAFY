# import sys
# sys.stdin = open('GNS_test_input.txt', 'r')
# sys.stdout = open('output_ladder1.txt', 'w')


def sort_pls(arr, n, number): # 입력받는 리스트, 그것의 개수, 넘버리스트

    for i in arr:
        min_idx = i
        for j in range(i+1, len(arr)):
            if number[i] < number[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr



T = int(input())

for tc in range(1, T+1):
    number = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9} # 인덱스 사용을 위한 리스트트
    num = list(map(int, input().split())) # 테스트케이스를 뺴기위해서서
    real_n = num[1] # 입력받는 숫자들의 개수 
    arr = list(map(int, input().split())) # 입력받는 숫자 리스트
    result = sort_pls(arr, real_n, number) 
    print(f'#{tc}')
    for i in range(real_n):
        print(i)



print('=====================================================')



# GPT 답변(내거 수정본)
def sort_pls(arr, n, number):  # 입력받는 리스트, 그것의 개수, 넘버리스트
    for i in range(len(arr)):  # 인덱스로 순회하도록 수정
        min_idx = i  # 최소값 인덱스 설정
        for j in range(i + 1, len(arr)):
            if number[arr[j]] < number[arr[min_idx]]:  # 비교할 때 딕셔너리 값 사용
                min_idx = j # 인덱스 업데이트
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 선택 정렬 수행
    return arr

T = int(input())

for tc in range(1, T + 1):
    number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 
              'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}  # 숫자 대응 딕셔너리
    
    input()  # 테스트케이스 번호와 개수 입력받기 (사용하지 않음)
    # 이런거 무시하는게 꿀팁이다. 
    arr = input().split()  # 입력받은 문자열 리스트

    result = sort_pls(arr, len(arr), number)  # 정렬 함수 호출

    print(f'#{tc}')
    print(" ".join(result))  # 공백을 기준으로 출력
    # 이런 방법도...

