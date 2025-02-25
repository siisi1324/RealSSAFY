# 매직메서드

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # 매직메서드 >> 특정 동작을 위한 메서드
    def __lt__(self, other):
        return self.grade < other.grade
    def __str__(self):
        return f'저는 {self.grade}학년 {self.name}입니다.'
    
a = Student('김싸피', 3)
b = Student('홍길동', 2)
print(a<b) 
# TypeError: '<' not supported between instances of 'Student' and 'Student'
# def __lt__(self, other)를 정의하니 비교가능해짐.
print(a)
# def __str__(self)를 정의하니 '저는 3학년 김싸피입니다.'로 출력됨.