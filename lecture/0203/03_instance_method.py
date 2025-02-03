# 메서드는 클래스 내부에 정의된 함수이다. 
# --> 클래스와 관련된 동작을 한다. 

# 메서드 종류 3가지
# 1. 인스턴스 메서드
# 주로 계속 사용해왔던 메서드의 종류
# 2. 클래스 메서드
# 3. 스태틱 메서드

# 인스턴스 메서드 구조
# 반드시 첫 번쨰 인자로 인스턴스 자신(self)를 받는다. 
# 'hello'.uppper() (사실 단축형 호출방식, 객체지향적 방식)
# 내부적으로 str.upper('hello') 이렇게 작동한다. 
# --> 그래서 첫번쨰 인자로 self를 받는다. 

class Counter:
    def __init__(self):
        self.count = 0
        # 생성자 함수도 인스턴스 함수다. (self없이는 동작하지 않는다.)
    def increment(self):
        self.count+=1

c = Counter()
print(c.count) #0
c.increment()
print(c.count) #1

c2 = Counter()
c.increment() 
# c가 increment를 한거지, c2는 아니다. 
print(c2.count) #0

# ---------------------------------------------------------------------

class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        # 서로에게 관련이 없다. 
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')
        # 인스턴스 변수의 name뿐이어서, self.name


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.
# == Person.greeting(person1)
