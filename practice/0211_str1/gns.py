# 그냥 무슨 정렬을 사용하던 정렬만 되면 된다.
# 강사님은 버블(n**2), 선택정렬 사용(n의 어느정도...)..(정렬만 사용, 리스트 생성 X)
# 언패킹으로 출력하는거 대박
# split() 이 리스트 반환하는 거 기억하기

# 딕셔너리 순서 사실은 있음...! keys


# GPT 답변(내거 수정본)
# 선택정렬

def sort_pls(arr, n, number):  # 입력받는 리스트, 그것의 개수, 넘버리스트
    for i in range(len(arr)-1):  # 인덱스로 순회하도록 수정
        # len(arr)-1 마지막 요소 전까지만 반복하면 되므로...
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
    # 다만 문자열로 받으니까 정수로 쓸일이 있으면 int화 시켜주기
    arr = input().split()  # 입력받은 문자열 리스트
    # 애초에 split자체가 리스트를 반환하니까 map, list 등등 필요없음.

    result = sort_pls(arr, len(arr), number)  # 정렬 함수 호출

    print(f'#{tc}')
    print(" ".join(result))  # 공백을 기준으로 출력
    # 이런 방법도...

print('=====================================================')

# count 정렬

# 제약조건 : value를 index로 사용이 가능해야 한다.
# 최소값과 최대값의 편차가 적어야 효율적이다. 
# 정렬된 배열을 반환하는 함수
# 각 요소 개수세서,그 개수 만큼 리스트에 갖다 붙이기


def solve(arr,N):
    num_cnt_dict = {
        'ZRO': 0,
        'ONE': 0,
        'TWO': 0,
        'THR': 0,
        'FOR': 0,
        'FIV': 0,
        'SIX': 0,
        'SVN': 0,
        'EGT': 0,
        'NIN': 0
    }
    for i in range(N):
        num_cnt_dict[arr[i]] += 1
    sorted_list = []
    for key in num_cnt_dict.keys():
        sorted_list += [key]*num_cnt_dict[key]
        # sorted_list.extend([key]*num_cnt_dict[key])
    return sorted_list


T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    # solve가 하위니까 N이 인자로 전달되지 않아도, 상수로 받아진다. 
    # 인자로 보내면 파라미터로 인식된다. 
    # 틀렸고, 글로벌 인자라 그렇다(global을 안쓰는 이유는 N을 바꾸지는 않아서 그렇다.)
    # 사실 arr도 이름만 똑같이 보낸다면 인자로 보내지 않아도 된다. 
    data = input().split()
    # selection_sort(data)
    data = solve(data,N)
    print(f'{tc}')
    print(*data)


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
    # 언패킹해서 출력하면 된다. ' '.join과 비슷

print('=====================================================')

# 조경호님 코드
def solve(NUM, word_lst):
    result = []
    for num in NUM:
        for word in word_lst:
            if word == num:
                result.append(num)
    return result
 
T = int(input())
for _ in range(1, T+1):
    NUM = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    tc, len_tc = input().split()
    # int(len_tc)
    word_lst = list(input().split())
    result = solve(NUM, word_lst)
    result = ' '.join(result)
    # solve(word)
    print(f'{tc}\n{result}')


