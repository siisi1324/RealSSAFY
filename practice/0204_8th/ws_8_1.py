class Animal:
    animal_of_num = 0
    
    def __init__(self):
        Animal.animal_of_num += 1


class Dog(Animal):
    def __init__(self):
        super().__init__()
    
    


class Cat(Animal):
    def __init__(self):
        super().__init__()
    


class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()

    @staticmethod
    def access_num_of_animal():
        return Animal.animal_of_num

    


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
