class Animal:
    animal_of_num = 0
    
    def __init__(self):
        Animal.animal_of_num += 1

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def meow(self):
        print('야옹!')

cat1 = Cat()
cat1.meow()