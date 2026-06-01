# 1. Local Variable : Declared inside a function.

def greet():
    message = "Hey"  # local variable
    print(message)

greet()

# 2. Global Variable : Declared outside all functions.

greeting = "Hey"  # global variable

def say_hi():
    print(greeting)

say_hi()