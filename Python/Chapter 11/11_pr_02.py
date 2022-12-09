class Animals:
    animalType = 'Mammal'

class Pets(Animals):
    color = 'White'

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bhow Bhow!")

d = Dog()
d.bark()
print(d.animalType)