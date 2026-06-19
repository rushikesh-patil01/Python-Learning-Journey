class Student:
    def __init__(self,name,age,marks):
        self.name = name   # Public
        self._age = age    # Protected
        self.__marks = marks # Private
        
    def display (self):
        print("Name :",self.name)
        print("Age: ",self._age)
        print("Marks: ",self.__marks)
        
s1 = Student ("Rushikesh", 22, 95)
print("Public :",s1.name)

print("protected :",s1._age)

s1.display()