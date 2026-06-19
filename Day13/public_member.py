# WAP to demonstrate a public member.

class Student:
    
    def __init__(self, name):
        self.name = name

s = Student("Rushikesh")

print(s.name)