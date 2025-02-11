
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
    
    input()
    # 이런거 무시하는게 꿀팁이다. 
    arr = input().split()  # 입력받은 문자열 리스트
    # 애초에 split자체가 리스트를 반환하니까 map, list 등등 필요없음.

    result = sort_pls(arr, len(arr), number)  # 정렬 함수 호출

    print(f'#{tc}')
    print(" ".join(result))  # 공백을 기준으로 출력
    # 이런 방법도...

print('=====================================================')

# 박준형님 코드
T = int(input())
for test_case in range(1, T+1):
    tc, N = input().split()

# tc, N = input().split() 
# '3', '5' (문자열)
    
# tc, N = map(int, input().split())
# 3, 5 (정수)
    N = int(N)
    # 그래서 한번더 정수화시킴
    num = list(input().split())
    num_dic = {"ZRO": 0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    num_list = []
     
     
    #숫자(value) 정렬하기 위해 리스트화
    for i in range(0,10):
        for j in range(N):
            if num_dic[num[j]] == i:
                num_list.append(num[j])
     
     
    print(f'#{test_case}')
    print(*num_list)
    # print(*num_list)는 리스트의 내용을 공백을 포함하여 출력.
