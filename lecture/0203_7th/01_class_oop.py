# 절차 지향 사고
# 예: 변수와 함수를 별개로 다룸
name = 'Alice'
age = 25


def introduce(name, age):
    print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')


introduce(name, age)


# 객체 지향 사고
# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')


alice = Person('Alice', 25)
alice.introduce()  # 객체가 자신의 정보를 출력
# 객체 지향은 수동적인 데이터가 능동적인 객체로 변화한 것

# 1️⃣ 클래스(Class)란?
# 객체를 만들기 위한 설계도(템플릿)
# 속성(데이터)과 동작(메서드)을 정의함

# 객체는 속성(변수)과 동작(메서드)을 가진다. 
# <class 'str'> 등에서의 class도 객체로써의 의미였다. 
# 객체는 고유한 특성을 가지고, 독립적이다. 
# 클래스 명은 파스칼 케이스방식으로 작성:
# snake_case 
# 대문자로시작, 단어시작마다 대문자(스타일 가이드)

# __init__ (초기화 ex. git init)
# 새로운 객체를 만들때만 자동 호출된다.

# 인스턴스 : 클래스를 통해 생성된 객체


name = 'Alice'

print(type(name)) # <class 'str'>

# 변수 name의 타입은 str클래스다.
# 변수 name은 str 클래스의 인스턴스이다.
# 우리가 사용해왔던 데이터 타입은 사실 모두 클래스였다. 
# str name의 메서드들은 class 'str'의 메서드였던 것이다. 
# ex. 'hello'.upper()
# == 문자열.대문자로()
# == 객체.행동()
# == 인스턴스.메서드()