class Dog:
    sound = '멍멍'
    def __init__(self):
        super().__init__()


class Cat:
    sound = '냐옹'
    def __init__(self):
        super().__init__()

class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

    
print(Pet())