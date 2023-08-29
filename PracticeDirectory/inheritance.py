class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Bow"


class Cat(Animal):
    def speak(self):
        return "meow"


dog = Dog("Canine")
cat = Cat("Feline")
print(cat.speak())
print(dog.speak())
