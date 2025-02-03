class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


p1 = Person()
p1.talk()  # unknown
# p1은 인스턴스 변수가 정의되저 있지 않아 클래스 변수 (Unknown)가 출력된다. 

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown
p2.name = 'Kim'
p2.talk()  # Kim

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim


# 독립적인 환경이 가장 중요하다. 
# 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능하다. 

# ----------------------------------------------

# 매직메서드(스페셜 메서드)

#  ----------------------------------------------

# 데코레이터(얘도 사실 함수)