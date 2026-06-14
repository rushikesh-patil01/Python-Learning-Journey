# WAP to demonstrate Runtime Polymorphism using Animal classes.

class Animal:
    
    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

class Cat(Animal):

    def sound(self):
        print("Cat Meows")

a1 = Dog()
a2 = Cat()

a1.sound() # Dog Barks
a2.sound() # Cat Meows