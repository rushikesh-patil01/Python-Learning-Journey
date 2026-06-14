# WAP to demonstrate Method Overloading using default arguments.

class Calculator:
    # Method with default parameter
    def add(self, a, b, c=0):
        return a + b + c

c = Calculator()
print(c.add(5, 10))      # Output: 15
print(c.add(5, 10, 15))  # Output: 30