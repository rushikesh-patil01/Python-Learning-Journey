# Day 7: Basics of Functions

# Q1. What is a Function in Python?
-> A function is a reusable block of code that performs a specific task.

# Parametrized vs Non-Parametrized Functions
# Non-Parametrized Function
- It doesn’t take any arguments.

Syntax:
def function_name():
    # code block

Example:
def greet():
    print("Hello, students!")

greet()

# Parametrized Function
--> Takes arguments (inputs) to perform operations.

Syntax:
def function_name(param1, param2):
    # code block

Example:
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# Q2. Why Do We Use Functions?
- Code Reusability
- Better Readability
- Reduces Code Duplication
- Easier Maintenance

# Q3. What is Function Definition?
-> Function definition means creating a function using the def keyword.

Syntax:
def function_name():
    # code

Example:
def greet():
    print("Welcome to Python")

# Q4. What is Function Calling?
-> Function calling means executing a function by using its name.

Example:
def greet():
    print("Hello")

greet()

# Q5. What are Function Arguments?
-> Arguments are values passed to a function.

Example:
def greet(name):
    print("Hello", name)

greet("Rushikesh")

# Q6. What are Default Arguments?
-> Default arguments provide a default value if no argument is passed.

Example:
def greet(name="Guest"):
    print("Hello", name)

greet()

Output:
Hello Guest

# Q7. What is a Return Statement?
-> The return statement sends a value back from a function.

Example:
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

Output: 30

# Q8. Difference Between print() and return()
print()	                return()

Displays output	        Sends value back
Cannot be reused	    Can be reused later
Used for display	    Used for processing

# Q9. Return Typed vs Non-Return Typed
# Non-Return Type Function
-> Only performs an action, does not return a value.

def add(a, b):
    print(a + b)

add(2, 3)  # Output: 5


# Return Type Function
-> Performs an action and returns a value using return.

def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5

# Q10. What is a Lambda Function?
-> A lambda function is a small one-line function without a name.

Syntax:
lambda arguments: expression

square = lambda X : X * X
print(square(5))

output:25 

Here: lambda x : x*x creates an anonymous function that squares its input


Example:
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

* Short Summary:
- Function = Reusable block of code
- def = Used to create a function
- Arguments = Values passed to a function
- Default Arguments = Predefined values
- Return = Sends value back
- Lambda = One-line anonymous function