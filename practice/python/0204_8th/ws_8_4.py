class Cat:
    def __init__(self):
        super().__init__()

    def meow(self):
        print('야옹!')

class Dog:
    def __init__(self):
        super().__init__()

    def bark(self):
        print('멍멍!')

class Pet(Cat, Dog):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound

    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(f'{self.sound}')


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
