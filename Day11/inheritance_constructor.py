# WAP to access Parent Constructor from Child Class.

class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    pass

c = Child()