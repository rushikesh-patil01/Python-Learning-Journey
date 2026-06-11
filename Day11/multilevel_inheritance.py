# WAP to demonstrate Multilevel Inheritance.

class Father:
    def father_info(self):
        print("This is Father")

class Mother:
    def mother_info(self):
        print("This is Mother")

class Child(Father, Mother):   # inherits from both
    def child_info(self):
        print("This is Child")

c1 = Child()
c1.father_info()
c1.mother_info()
c1.child_info()

