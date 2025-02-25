# 버그
# 디버깅
# = 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정, 프로그램의 오작동 원인을 식별하여 수정하는 작업

# 1) print 함수 활용
# 2) IDE의 기능 활용
# 3) python tutor 활용

# 에러

# 1) 문법 에러(Syntax Error)

# (1) EOL(End of Line)
# (2) EOF(End of File)

# 2) 예외

# 내장 예외 - 상속구조를 갖추고 있다.

# ===========================================================================

# 예외처리

# try - 예외가 발생할 수 있는 코드 작성
# except 

# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')


try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')


# 복수 예외처리
try: 
    num = int(input('숫자입력 : '))
    print(100/num)
except (ValueError, ZeroDivisionError):
    print('제대로 입력하렴')



try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자입력력')
except ZeroDivisionError:
    print('0으론 못나눠')
except:
    print('오류가 발생했습니다.')


# else
# finally
# finally와 그냥 적는 것의 차이 : 
# finally를 적으면 정상종료시에도(return) 출력이 된다.

try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')

# ==============================================================

# 내장예외는 상속 계층구조를 가지고 있으므로, 상위 예외를 이용하면 다른 하위 예외에는 도달하지 못한다. 
# ex. BaseException은 모든 예외의 최상위 예외다.

# 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함
# ZeroDivisionError 클래스는 BaseException 클래스의 하위 클래스 중 하나이므로 ZeroDivisionError를 먼저 작성해야 함
# https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except BaseException:
    print('숫자를 넣어주세요.')
# ZeroDivisionError는 BaseException의 하위 클래스이므로 BaseException보다 먼저 작성해야 함
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')


# 옳은 코드
# 가장 구체적인 예외부터 처리하고, 마지막에 범용 예외를 처리하도록 순서를 배치
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
# 1) 구체적인 예외부터
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('숫자를 넣어주세요.')
# 2) 마지막에 광범위한 예외(Exception)
except Exception:
# BaseException보다 쓰기를 추천
    print('에러가 발생하였습니다.')

# as키워드

my_list = []

try:
    number = my_list[1]
except IndexError as error:
    # list index out of range가 발생했습니다.
    print(f'{error}가 발생했습니다.')

# try - except와 if - else 를 함께 사용할 수 있다. 


# try:
#     while:
#      예외
# except:
#     pass

# ==============================================================================


my_dict = {'key': 'value'}

# EAFP (Easier to Ask for Forgiveness than Permission, 허락보다 용서 구하기)
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')
# 큰 프로젝트나 등등에서 사용된다.


# LBYL (Look Before You Leap, 돌다리도 두들겨보고 건너기)
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
# 보통은 if-else문을 쓴다. 
