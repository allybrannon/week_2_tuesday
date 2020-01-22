class Cat:
    #class attribute
    species = 'mammal'
    legs = 4
    eyes = 2
    tail = 1

    #initialize/instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

gus = Cat("Gus", 8)
print(gus.description())
oreo = Cat("Oreo", 17)
print(oreo.description())