# <string>
# <컴퓨터에서의 문자표현>

# 파이썬에서는 별도의 char 타입이 없고, 텍스트 데이터의 취급방법이 통일되어 있다. 
# 기호 : '', "", ''' ''', """ """ 
# + 로 문자열끼리 연결할 수 있고, * 정수로 문자열 반복이 가능하다. 



# [아스키코드](7비트, 128문자를 표현)
# 확장 아스키코드 
# - 표준 문자 이외의 악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적인 문자를 추가한 부호
# - 8비트 사용 (추가적인 128개의 문자)
# - but 표준 아스키와는 다르게, 다른 확장 아스키는 교환이 비교적으로 어려웠다. (추가해독 필요)

# 아스키코드의 한계(각 나라간의 코드체계 이해필요)
# - 유니코드(다국어 처리 표준)의 발현



# [유니코드]
# 아스키코드를 연장하면서(숫자 유지) 추가적으로 확장시켰다. 

# just 구경하기
# print(f'{ord("대"):x}') #0xb300
# print(chr(0xb300)) # 대대

# 유니코드도 USC-2, USC-4 두 가지 버전이 있어서 바이트 순서에 대한 표준화가 부족하다. 
# 따라서 각 경우를 위한 외부 인코딩이 필요한한 문제가 발생한다. 
# big-endian, little-endian 할당을 큰 숫자부터 할거냐, 작은 숫자부터 할거냐.. 
# 지금은 주로 llittle-endian 사용

# 유니코드 인코딩 (UTF : Unicode Transformation Format)
# UTF-8(가변 : 1-4바이트), UTF-16(가변 : 2-4바이트), UTF-32(고정 : 4바이트(메모리낭비가 클 수 있다는 단점)) 

# (파이썬 인코딩 방식을 지정해줄 수 있다~)



# [참고 : 문자열은 안에만 변경할 수는 없다.]
s1 = list(input())  #abc
print(s1)  #['a', 'b', 'c']
s2 = input() #abc
print(s2) #abc
print(s1[1]) #b
print(s2[1]) #b
s1[1] = 'e' 
print(s1) # 리스트니까 가능
s2[1] = 'e'
print(s2) # 문자열은 immutable


print('=====================================================')

# [문자열 곱하기, 연결하기(join)]
s1 = 'ab'*6
print(s1) #abababababab
s = ['a', 'b', 'c']
print(''.join(s)) #abc
# 자주쓰는 방식이니 이해, 암기하기

print('=====================================================')


# [Index를 이용해서 문자열 뒤집기]
txt = list(input())
N = len(txt)
for i in range(N//2):
    txt[i], txt[N-1-i] = txt[N-1-i], txt[i]
print(txt)

print('=====================================================')

# <연습문제 1>
# [reverse, join 활용]
s = 'string'
s = s[::-1]
print(s, type(s))  # gnirts <class 'str'>

s_list = list(s)
s_list.reverse()
print(s_list)  # ['s', 't', 'r', 'i', 'n', 'g']

# 올바른 join 사용법
print("".join(s_list))  # string

print('=====================================================')

# <연습문제2>
# 8*8 평면 글자판에서 제시된 길이 만큼의 회문(거꾸로 읽어도 똑같은 문장이나 낱말)의 개수를 구해라

# 4
# CBBCBAAB
# CCCBABCB
# BAAAACAB
# BACCCCAC
# AABCBBAC
# ACAACABC
# BCCBAABC
# ABBBCCAA


N = int(input())
txt = input()
total = 0
for j in range(8-N+1): # 회문을 확인하는 구간의 첫 글자 인덱스스
    for k in range(N//2): # 회문의 길이 절반만큼 비교
        if txt[j+k] != txt[j+N-1-k]:
            break # 비교 글자가 다르면 현재구간 중지
    else: #break없이 걸리지 않고 for문 종료
        total += 1
print(total)
