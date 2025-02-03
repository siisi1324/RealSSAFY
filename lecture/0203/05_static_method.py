# == 정적 메서드
# 클래스와도 인스턴스와도 상관없는 독립적인 동적을 위한 메서드
# @staticmethod 데코레이터를 사용하여 정의
# 호출 시 자동으로 전달 받는 인자가 없음
# 인스턴스나 클래스 속성에 직접 접근하지 않는, '도우미 함수'와 비슷한 역할 
# == helper함수로도 불린다. 

class MathUtils:
    @staticmethod
    def add(a, b):
        return a+b
    
print(MathUtils.add(3, 5))  #8
# 호출 자체는 class에서 한다.