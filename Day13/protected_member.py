# WAP to demonstrate a protected member.

class Student:
    
    def __init__(self, name):
        self._name = name

class Child(Student):

    def display(self):
        print(self._name)

c = Child("Rushikesh")

c.display()