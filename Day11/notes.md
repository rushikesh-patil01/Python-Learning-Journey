# Day 11 - Object Oriented Programming (OOP) in Python

# Inheritance in Python (OOP)

# Q1.What is Inheritance?
-> Inheritance is an OOP feature that allows one class to use the properties and methods of another class.

- The class that gives its features is called the Parent (Base, Super) Class.

- The class that receives the features is called the Child (Derived, Sub) Class.

- Inheritance helps with code reusability (we don’t repeat the same code in every class).

- In short: Child class can reuse and extend parent class features.

# Syntax of Inheritance
class ParentClass:
    # parent methods and variables

class ChildClass(ParentClass):
    # child methods and variables

# Q3. Why Inheritance is Used?
-> To reuse code instead of writing it again.

- To build a hierarchy of classes (like parent → child → grandchild).

- To implement real-world relationships (e.g., Teacher is a Person, Car is a Vehicle).

- To make programs organized, modular, and maintainable.

# Q4. 4.Types of Inheritance in Python
- Python supports 5 main types of inheritance:

1.Single Inheritance

2.Multiple Inheritance

3.Multilevel Inheritance

4.Hierarchical Inheritance

5.Hybrid Inheritance

# Explanation of Each Type :

# 1. Single Inheritance
-> Definition: One child class inherits from one parent class.

Syntax:

class Parent:
    # parent code

class Child(Parent):
    # child code

# 2. Multiple Inheritance
-> Definition: One child class inherits from multiple parent classes.

Syntax:

class Parent1:
    # code

class Parent2:
    # code

class Child(Parent1, Parent2):
    # child code


# 3. Multilevel Inheritance
-> Definition: A child class inherits from a parent class, and then another child inherits from that child (grandchild).

Syntax:

class GrandParent:
    # code

class Parent(GrandParent):
    # code

class Child(Parent):
    # code

# 4. Hierarchical Inheritance

Definition:

Multiple child classes inherit from the same parent class.

Syntax:

class Parent:
    # parent code

class Child1(Parent):
    # code

class Child2(Parent):
    # code


# 5. Hybrid Inheritance

Definition:

A combination of two or more types of inheritance (e.g., Single + Multiple).

Example:

class A:
    def displayA(self):
        print("Class A")

class B(A):
    def displayB(self):
        print("Class B")

class C:
    def displayC(self):
        print("Class C")

class D(B, C):   # Hybrid (Multilevel + Multiple)
    def displayD(self):
        print("Class D")

d1 = D()
d1.displayA()
d1.displayB()
d1.displayC()
d1.displayD()


Output:

Class A
Class B
Class C
Class D

========================================================================================================
# Final Short Recap

- Inheritance = mechanism where one class inherits from another.

- Why used? → Code reusability, hierarchy, easy maintenance.

- Types of Inheritance:

- Single → one parent → one child.

- Multiple → one child → multiple parents.

- Multilevel → parent → child → grandchild.

- Hierarchical → one parent → multiple children.

- Hybrid → combination of above types.