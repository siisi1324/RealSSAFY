# <연산>
# <문자열 비교>

# 파이썬에서는 == 연산자와 IS 연산자를 제공한다. 
s1 = 'abc'
s2 = 'ab'
s3 = 'def'
s4 = s2 + 'c'

print(s1==s4) # True 같은모양인가?
print(s1 is s4) # False 같은 메모리 위치인가?
print(s1 is 'abc') # True

# 문자열 interning이란?
# Python은 같은 문자열을 여러 번 생성하는 것을 방지하기 위해 짧은 문자열을 미리 캐싱(저장) 해둠.
# 즉, 'abc' 같은 짧은 문자열은 메모리에 한 번만 저장되므로 동일한 객체를 참조하게 됨.
# 그래서 print(s1 is 'abc') # True

print('=====================================================')


s1 = 'ab'
s2 = 'ab'
s3 = 'ac'
s4 = 'AB'
print(s1==s2) #True
print(s1 < s2) #False
print(s1 < s3) #True
print(s2 < s4) #False
# 사전순서상 문자열의 크기를 비교한다. 
# 대문자가 사전순서상 먼저 오므로 소문자보다 크기가 작다. 
# 스페이스가 가장 순서가 빠르다, 대문자, 소문자 순...등등

# 잠만 순서가 빠른게 큰거야??? 
# -> 순서가 빠른게 당연히 작다. 

print('A' < '@') #False
# 특수기호가 더 먼저 온다(작다).

print('=====================================================')

# 16진수 문자 'F'를 10진수로 변환
a = 'F'       # 'F'는 16진수에서 10진수로 변환하면 15 (F = 15)
b = int(a, 16)  # int(문자열, 진수): 'F'를 16진수로 해석하여 10진수로 변환

# 2진수 문자열 '1001'을 10진수로 변환
c = '1001'      # 2진수 1001은 10진수로 변환하면 9 (1×2³ + 0×2² + 0×2¹ + 1×2⁰ = 9)
d = int(c, 2)   # int(문자열, 진수): '1001'을 2진수로 해석하여 10진수로 변환

# 변환된 10진수 값 출력
print(b)  # 출력: 15
print(d)  # 출력: 9


print('=====================================================')

# 숫자형태의 문자열을 인자로 받아서 정수를 반환하는 함수
# int, str 과 동일한 역할
# ord(문자) : 문자의 아스키코드에 대응하는 숫자 반환
# chr(숫자) : 숫자의 문자 반환

def atoi(s):
    i = 0  # 변환된 정수를 저장할 변수

    for x in s:  
        # ord(x): 문자 x의 아스키(유니코드) 값
        # ord('0'): 숫자 '0'의 아스키 값 (48)
        # 예: '3'의 아스키 값은 51 -> ord('3') - ord('0') = 51 - 48 = 3
        i = i * 10 + (ord(x) - ord('0'))  
    return i  # 최종 변환된 정수 반환

# 문자열 '123'을 정수로 변환
s = '123'
a = atoi(s) 
print(a) # 123

print('=====================================================')

def itoa(n):
    i = ''
    while n > 0:
        s = n%10
        i = i + chr(s+ord('0'))
        # 문자 0의 값을 찾아야 하므로 '0'을 넣어야 함
        n = n//10
    return i

def itoa(number):
    result = ''
    while number>0 :
        remain = number % 10
        number = number // 10
        result += chr(1 + ord('0'))
    return result






