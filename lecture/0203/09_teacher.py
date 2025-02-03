# 객체지향 프로그래밍 vs 절차지향 프로그래밍


# 절차지향 프로그램
# 데이터와 명령어의 순서가 중요
# 예) 로또 번호 생성 프로그램 

# 1. 1부터 45까지 숫자중에 하나 뽑아서 numbers에 넣기
# 2. numbers의 크기가 6이 될때까지 1반복
# 3. 출력

# =========================================================

# 로또번호를 만드려면 로또번호 생성기가 있어야 함
# 출력, 번호 추출, 중복 검사, 등등
# 로또번호 생성기가 해야할 일을 위주로 생각한 것 = 객체지향적


# ----------------------------------------------------------

# 절차 지향 예시
# 중복되지 않는 숫자 6개를 저장하기 위한 데이터 선언
import random

numbers = set()
# 1이상 45 이하의 정수중 임의의 수를 numbers에 추가
# set에 숫자추가 : add

while len(numbers)<6:
    numbers.add(random.randint(1, 45))

numbers = list(numbers)
numbers.sort()
# set은 시퀀스(순서가 있는 것)가 아니기 때문에 정렬이라는 것이 없다. 따라서 list로 변환 후 정렬
print(numbers)

#-------------------------------------------------------------

# 객체(object, data와 method를 가지는 것) 지향 예시

# 객체와 인스턴스의 차이:
# a = {'a':'apple'}
# b = [1,2,3,5]
# c = 'hello '
# a, b, c는 객체이다. 딕셔너리, 리스트, 스트링의 인스턴스다. 


# numbers : 숫자 6개 저장하기 위한 변수
# 인스턴스 변수는 어떻게 만들어요?
# pick_numbers() : 숫자 6개 뽑는 동작
# sort() : 정렬
# print() : 출력

# class LottoMaker:
#     def __init__(self, num):
#         self.a = num
#         # a는 인스턴스 변수다.
    
# inst1 = LottoMaker(10)
# inst2 = LottoMaker(50)
# print(inst1.a)
# print(inst2.a)

class LottoMaker:
    company = 'SSAFY'
    # 객체가 가지는 상태(속성)은 변수로 선언
    def __init__(self):
        self.numbers = set()
    # 객체가 가지는 동작(행동)은 메서드(함수)로 선언
    # 인스턴스 메서드 : 첫 번째 인자가 'self'인 메서드, 
    #                  인스턴스 변수를 활용해서 동작
    def pick_numbers(self):
        while len(self.numbers)<6:
            self.numbers.add(random.randint(1, 45))

    def sort(self):
        # self.numbers = self.numbers.sort()
        # self.numbers = list(self.numbers).sort()
        self.numbers = list(self.numbers)
        self.numbers.sort()

    def lotto_print(self):
        print(self.numbers)

inst1 = LottoMaker()
inst1.pick_numbers()
inst1.sort()
inst1.lotto_print()






