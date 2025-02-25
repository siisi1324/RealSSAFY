class Animal:
    animal_of_num = 0
    
    def __init__(self):
        Animal.animal_of_num += 1


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        print('멍멍!')


dog1 = Dog()
dog1.bark()