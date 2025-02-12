class Circle:
    # 클래스변수
    # 모든 인스턴스가 공유하는 속성, 클래스 내부에서 직접 정의
    pi = 3.14
    # 생성자 메서드
    def __init__(self, radius):
        # radius를 반드시 작성해줘야 인스턴스가 발생(위치인자는 반드시 채워야)
        self.radius = radius

        


# 인스턴스 생성
# c1 = Circle()
# TypeError: __init__() missing 1 required positional argument: 'radius'

c1 = Circle(1)
c2 = Circle(5)

# 인스턴스 변수(속성)
print(c1.radius)
print(c2.radius)


# 클래스 변수(속성)
print(c1.pi)
print(c2.pi)


# ------------------------------------------------------------------------------------
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10

# c1의 인스턴스 변수 pi를 생성
c1.pi = 100

print(c1.pi)  #100
print(Circle.pi)  #3.14
# 인스턴스 자신에게서 먼저 찾는다, 그 다음에 클래스 영역에서 찾는다. 
# c2는 자신의 인스턴스에 pi가 없어서 클래스 영역에서 찾는다. 

# c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print()  #
