# WAP to demonstrate Duck Typing.

class Duck:

    def sound(self):
        print("Quack Quack")

class Dog:

    def sound(self):
        print("Bark Bark")

def make_sound(obj):
    obj.sound()

make_sound(Duck())
make_sound(Dog())