class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"


def make_animal_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()
bird = Bird()

# Using polymorphism to make animals speak
print(make_animal_speak(dog))
print(make_animal_speak(cat))
print(make_animal_speak(bird))
