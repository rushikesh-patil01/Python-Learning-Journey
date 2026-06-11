# WAP to demonstrate Single Inheritance.

class Parent:
    def display(self):
        print("I am Parent Class")

class Child(Parent):
    pass

c = Child()

c.display()

#------------------------------------------------

class Person:
    def display(self):
        print("I am a Person")

class Student(Person):   # inherits from Person
    def study(self):
        print("I am studying")

s1 = Student()
s1.display()
s1.study()
