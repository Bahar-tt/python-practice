from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "WOOF!"
    
    def move(self):
        return " The Dog Runs!"
    
class Cat(Animal):
    def make_sound(self):
        return "MEOW!"
    
    def move(self):
        return "The Cat Walk & Runs!"
    
class Cow(Animal):
    def make_sound(self):
        return "MAA!"
    
    def move(self):
        return "The Cow Walk!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print([animal.make_sound() , animal.move()])