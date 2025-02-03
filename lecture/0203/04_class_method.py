class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()
        # 인스턴스를 생성할 때마다 자동으로 실행된다. 

    @classmethod
    def increase_population(cls):
        cls.population += 1

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  #

Person.increase_population()
print(Person.increase_population)