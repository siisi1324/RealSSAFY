# 객체지향 5대원칙
# solid
# LSP 리스코프 치환 원칙, 느슨한 결합

# 오버라이딩과 오버로딩의 차이는 상속의 차이
# 오버라이딩 : 상속받은 클래스의 메서드가 이름이 같을 때
# 메서드 오버라이딩 : 부모클래스에 정의된 메서드를 자식클래스에서 재정의
# 재정의 : 이름과 매개변수가 같은 메서드를 작성하는것
# 오버로딩 : 같은 클래스에서 변수가 다르고 이름만 같을 때(파이썬에서는 문제가 없다.)


class Animal:
    def eat(self):
        print('냠냠 먹어요')
    
class Dog(Animal):
    def sound(self):
        print('멍멍')

class cat(Animal):
    def sound(self):
        print('야옹')


class zoo:
    def __init__(self, animal:Animal):
        self.animal = animal

    def make_sound(self):
        self.animal = animal

# zoo는 animal의 의존한다.


dog1 = Dog()
cat1 = cat()

# Inversion of Control(제어역전), Dependency Injection(의존성주입) (시험엔 안나옴)
zoo = zoo(dog1)
zoo2 = zoo(cat1)
zoo.make_sound()
zoo2.make_sound()

dog1.eat()

# 우리 프로그램을 실행 때는 Animal instance 가 하나 필요하다. 



# ==================================================================================
# 다중상속

