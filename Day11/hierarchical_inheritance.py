# WAP to demonstrate Hierarchical Inheritance.

class Parent:

    def display(self):
        print("Parent Class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()

c1.display()
c2.display()


#--------------------------------------------------------------

class Parent:
    def parent_info(self):
        print("This is Parent")

class Child1(Parent):
    def child1_info(self):
        print("This is Child 1")

class Child2(Parent):
    def child2_info(self):
        print("This is Child 2")

c1 = Child1()
c2 = Child2()

c1.parent_info()
c1.child1_info()

c2.parent_info()
c2.child2_info()
