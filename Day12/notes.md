# Day 12 : Polymorphism in Python (oops)

# Q1. Definition
-> Polymorphism means “one name, many forms”.

- In Python, it allows the same method or function to behave differently depending on the object or arguments.

# Q2. Why we use it:
- Makes code flexible and reusable
- Makes programs clean and readable

# Q3. Types of Polymorphism
-> Python mainly uses two types:

1. Compile-time Polymorphism (via method overloading simulation)

2. Runtime Polymorphism (via method overriding)

# 1. Compile-time Polymorphism (Method Overloading)

-> Method Overloading means creating multiple methods with the same name but different parameters.

Python does not support true method overloading like Java.

It can be simulated using:
- Default arguments
- *args
- **kwargs

Syntax
def method_name(param1, param2=0):
    # code

Example
class Calculator:
    # Method with default parameter
    def add(self, a, b, c=0):
        return a + b + c

c = Calculator()
print(c.add(5, 10))      # Output: 15
print(c.add(5, 10, 15))  # Output: 30


Explanation:

Same method add() can work with 2 or 3 numbers

Python decides at runtime which arguments are given

- Why we use it

Avoids writing multiple method names for similar tasks

Makes code simpler and cleaner

# 2. Runtime Polymorphism (Method Overriding)
-> Method Overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

Achieved using inheritance

Child class can override parent method

Syntax
class Parent:
    def method_name(self):
        # parent code

class Child(Parent):
    def method_name(self):
        # child code

Example
class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

d = Dog()

d.sound()

# Q4. Does Python Support Method Overloading?

-> No, Python does not support traditional method overloading.

Instead, Python uses:
- Default Parameters
- Variable Length Arguments (*args)

Example:

class Demo:

    def show(self, a, b=0):
        print(a + b)

---------------------------------------------------
# Explanation:
- Same method sound() behaves differently depending on the object type

- Python decides which method to call at runtime

- Why we use Method Overriding

- Allows child class to change or extend behavior

- Makes code flexible and reusable

- Supports runtime polymorphism


# Q5. What is Runtime Polymorphism?
-> Runtime Polymorphism is achieved through Method Overriding.
- The method to execute is decided at runtime based on the object.

Example:

dog = Dog()
dog.sound()

Output: Dog Barks

# Q6. What is Compile-Time Polymorphism?
-> Compile-Time Polymorphism is achieved through Method Overloading.

Since Python doesn't support true method overloading, it is simulated using default arguments.

# Q7. Difference Between Overloading and Overriding?

Method Overloading:
- Same method name
- Different parameters
- Same class
- Compile-time concept

Method Overriding:
- Same method name
- Same parameters
- Parent and Child classes
- Runtime concept


# Q8. What is Duck Typing in Python?
-> Duck Typing means Python focuses on an object's behavior rather than its type.

- "If it walks like a duck and quacks like a duck, then it is a duck."

# Q9. What is Operator Overloading?
-> Operator Overloading allows operators to behave differently for user-defined objects.

Example:

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

# Q10. What is MRO (Method Resolution Order)?
-> MRO defines the order in which Python searches for methods in inheritance.

It is especially important in Multiple Inheritance.

# Q11. What are the Advantages of Polymorphism?
-> Advantages of Polymorphism:

- Code Reusability
- Flexibility
- Easy Maintenance
- Better Readability
- Extensibility
- Supports OOP Principles


# Q12. What is Dynamic Binding?
-> Dynamic Binding means the method to be executed is determined at runtime rather than compile time.

- It is closely related to Method Overriding and Runtime Polymorphism.



