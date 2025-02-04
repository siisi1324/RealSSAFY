class Animal:
    def eat(self):
        print('먹는 중')


class Dog(Animal):
    # Animal클래스를 인자로 가지는 하위 클래스(이름만 인자로 넣으면 상속이 된다. )
    # 부모의 모든 클래스를 가진다. (ex. eat마저)
    def bark(self):
        print('멍멍')

# 인스턴스 생성성
my_dog = Dog()


# 인스턴스 메서드 호출출
my_dog.bark()  # 멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat() # 먹는 중

# =======================================================================

# 메서드 오버라이딩
# = 부모 클래스의 메서드를 자식 클래스에서도 같은 이름, 같은 파라미터 구조로 재정의하는 것
# 자식의 메서드를 먼저 실행한다. 
# 오버로딩(같은 이름의 메서드를 정의하면, 뒤에 것만 인식한다. )

class Animal:
    def eat(self):
        print('Animal이 먹는 중')


class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print('Dog가 먹는 중')


my_dog = Dog()

my_dog.eat()  # Dog가 먹는 중


# 오버로딩 (파이썬 미지원)
class Example:
    def do_something(self, x):
        print('첫 번째 do_something 메서드:', x)

    # 파이썬에서는 메서드가 "이름"이 같으면 앞선 정의를 덮어써버림
    def do_something(self, x, y):
        print('두 번째 do_something 메서드:', x, y)


example = Example()
# TypeError: do_something() missing 1 required positional argument: 'y'
example.do_something(10)


# ========================================================================

# 다중 상속
# 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
# 상속받은 모든 클래스의 요소를 활용 가능함
# 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    # Dad를 먼저 상속받았으므로, 중복된 속성이나 메서드가 있으면 Dad의 속성을 먼저 상속받는다. 
    # MRO(Method Resolution Order) 알고리즘을 이용해서 Dad -> Mom -> Person 순으로 상속.
    # MRO가 깊이 탐색과 연관있는 것 같음.
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY
# Dad를 먼저 상속받았으므로, 중복된 속성이나 메서드가 있으면 Dad의 속성을 먼저 상속받는다. 

# ========================================================================================

#  Super() 메서드


#  1) 단일상속에서의 super()

# super를 사용할 때
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # super()를 통해 Person의 __init__ 메서드 호출
        super().__init__(name, age, number, email)
        # Person.__init__(name, age, number, email)
        # 와 같은 동작을 하고 실행도 된다. 
        # 단일 상속에서는 super()과 Person()이 같다. 
        # But 부모 클래스의 이름이 바뀐다면.. super()이 유리
        self.student_id = student_id


# super를 사용하지 않았을 때
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id



#  2) 다중상속에서의 super()

# 다중 상속

class ParentA:
    def __init__(self):
        super().__init__()
        # 중요한 파트
        # 상속이 끊기지 않도록...
        # 모든 클래스의 최상위 클래스 'object' (아직은 참고만 하기)
        # 여기서의 super().__init__()는 B
        # child에서의 MRO순서를 보장하기 때문에(child-A-B)
        # ParentA에서의 super()은 object로..(아마)
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  
        # 다중상속 상의 MRO 순서에 따라 ParentsA를 상속
        # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')


child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""

print(child.value_c)  # Child
print(child.value_a)  # ParentA
print(
    child.value_b
)  
# AttributeError: 'Child' object has no attribute 'value_b'
# super()가 ParentA에서 상속이 끊긴다.


"""
<ParentA에 super().__init__()를 추가하면?>
그 다음으로 ParentB의 __init__가 실행되어 value_b도 초기화할 수 있음
그러면 print(child.value_b)는 ParentB를 출력하게 됨

print(child.value_b)  # ParentB
"""

"""
<Child 클래스의 MRO>
Child -> ParentA -> ParentB

super()는 단순히 “직계 부모 클래스를 가리킨다”가 아니라, 
MRO 순서를 기반으로 “현재 클래스의 다음 순서” 클래스(또는 메서드)를 가리킴

따라서 ParentA에서 super()를 부르면 MRO상 다음 클래스인 ParentB.__init__()가 호출됨
"""


"""
1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
    1.	child = Child() 호출 시, Child.__init__()가 실행
    2.	Child.__init__() 내부에서 super().__init__()를 호출
        - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
    3.	ParentA.__init__()로 진입

1.2. ParentA.__init__() 내부
	1.	ParentA.__init__()에는 다시 super().__init__()가 있음
	2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
    3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
	4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
	5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
	6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료

1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
	- child.value_a → 'ParentA'
	- child.value_b → 'ParentB' 
	- child.value_c → 'Child'
"""

# ==================================================================================

class A:
    def __init__(self):
        print('A Constructor')


class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')


class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')


# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)
