# WAP to use getter and setter methods to access a private variable

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self._age = age
        self.__marks = marks
        
# getter method
    def get_marks(self):
        return self.__marks
    
# setter method
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks, must be between 0 to 100")

    def display(self):
        print("Name:",self.name)
        print("Age:",self._age)
        print("Marks:", self.__marks)
        
s1 = Student("Rushikesh", 22, 98)

print("Private:",s1.name)
print("Protected:",s1._age)

print("Public:",s1.get_marks())
        
# Update Marks
s1.set_marks(99)
print("Update marks:",s1.get_marks())












