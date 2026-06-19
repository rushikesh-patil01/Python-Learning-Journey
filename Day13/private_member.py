# WAP to demonstrate a private member.

class Student:

    def __init__(self, name):
        self.__name = name

    def show(self):
        print(self.__name)

s = Student("Rushikesh")

s.show()