# Day 8 - Advanced Python Concepts (HOF, Scope, Recursion, Iterators, Generators & Decorators)

# Higher Order Functions (HOF) in Python
# Q1. What is a Higher Order Function?
-> A Higher Order Function is a function that can do any one (or both) of these:
Takes another function as input (argument)
Returns another function as output

In short:
Functions that work with other functions!

Example 1 – Function as Argument
def greet(name):
    return f"Hello, {name}"

def loud(func):   # takes function as input
    def wrapper(name):
        return func(name).upper()
    return wrapper

shout = loud(greet)   # passing function
print(shout("Rahul"))   # HELLO, RAHUL


Here: loud is a higher order function because it takes another function (greet) as input.

# Q2. Built-in Higher Order Functions in Python
-> Python already gives us some HOFs that we use every day

# - map() – applies a function to each element

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print(squares)   # [1, 4, 9, 16]


# - filter() – keeps only elements that match condition

numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [10, 20, 30]


# - reduce() – combines all elements into one value

from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)
print(total)   # 10


# - sorted() with key= – key takes a function

names = ["Rahul", "Priya", "Amit"]
sorted_names = sorted(names, key=lambda n: len(n))
print(sorted_names)   # ['Amit', 'Rahul', 'Priya']

# Q3. Why are HOFs Useful?

They make code shorter and cleaner 

They allow functions to be reused easily 

They are the foundation for functional programming 

# Q4. Simple Rules for Students

A function is higher order if:

It takes a function OR

It returns a function

Not every function is a higher order function.

=======================================================================================================

# Q5.  enumerate()
-> enumerate() adds a counter (index number) to items in a list (or any iterable).
It’s useful when you want both index and value while looping.

Example
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


Output:
0 apple
1 banana
2 cherry
--------------------------------------------------------------------------------------------------------
-> By default, counting starts at 0, but you can start at any number:

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


Output:
1 apple
2 banana
3 cherry

# zip() joins two or more lists element by element.
-> Think of it like a zipper that combines items together.

Example
names = ["Rahul", "Priya", "Amit"]
marks = [85, 92, 78]

for n, m in zip(names, marks):
    print(n, m)


Output:
Rahul 85
Priya 92
Amit 78


# If lists have different lengths, zip() stops at the shortest list.

Example
a = [1, 2, 3]
b = [10, 20]

print(list(zip(a, b)))


 Output:

[(1, 10), (2, 20)]


# Q6. what is eval()

eval() takes a string and runs it as Python code.

Be careful! It can run any code, so it’s dangerous with unknown input.

Example
x = 10
expression = "x * 5 + 2"
result = eval(expression)
print(result)

Output:
52


Another Example:
print(eval("2 + 3"))        # 5
print(eval("max(10, 20)"))  # 20

-------------------------------------------------------------------------------------------------

Quick Summary for Students

enumerate() → Adds index number while looping.

zip() → Joins lists together like a zipper.

eval() → Runs a string as Python code (use carefully).

====================================================================================================
# Scope in Python 

# Q7. 1. What is Scope?
-> Scope means the area in a program where a variable is available (can be used).
When we create variables inside or outside a function, their scope decides who can access them.

# Q8. Types of Scope in Functions (LEGB Rule)
-> Python follows the LEGB rule:

- Local (L) – Inside the current function

- Enclosing (E) – Inside outer functions (for nested functions)

- Global (G) – Outside all functions (main program)

- Built-in (B) – Python’s built-in names (len, sum, print …)

# Examples :
A) Local Scope
-> Variables created inside a function are local — they exist only in that function.

def my_func():
    x = 10   # local variable
    print("Inside function:", x)

my_func()
print("Outside function:", x)   # Error: x not defined

B) Global Scope
-> Variables created outside all functions are global — they can be used anywhere.

x = 100   # global variable

def my_func():
    print("Inside function:", x)

my_func()
print("Outside function:", x)


Output:
Inside function: 100
Outside function: 100

C) Enclosing Scope (Nested Functions)
-> Inner function can use variables from the outer function.

def outer():
    y = 20   # enclosing variable
    
    def inner():
        print("Inner function:", y)
    
    inner()

outer()


Output:
Inner function: 20

D) Built-in Scope
-> Python has some built-in variables/functions that are always available.

print(len([1, 2, 3]))   # 3  (len is built-in)


# Q9. Special Keywords
# - global keyword

Used when you want to modify a global variable inside a function.

count = 0   # global variable

def increase():
    global count
    count += 1

increase()
print(count)   # 1

# - nonlocal keyword

Used when you want to modify a variable from an enclosing function (outer but not global).

def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print("Inner:", x)
    inner()

outer()


Output:
Inner: 6

------------------------------------------------------------------------------------------------
# Quick Summary 

Local → Inside the current function.

Enclosing → Outer function (for nested functions).

Global → Defined outside all functions.

Built-in → Python’s reserved names.

Order of search (LEGB): Local → Enclosing → Global → Built-in.


# Recursion in Python (Step by Step for Students)
# Q10. What is Recursion?
-> Recursion is when a function calls itself to solve a problem.
It keeps calling until a stopping condition (called base case) is reached.

Think of it like:
A mirror facing another mirror  (repeats again and again).
Or breaking a big problem into smaller copies of the same problem.

# -> Syntax of a Recursive Function
def function_name(parameters):
    if stopping_condition:        # base case
        return some_value         # stop recursion
    else:
        return function_name(smaller_problem)


stopping_condition (base case) → Very important! Tells recursion when to stop.
Without it → function calls itself forever → program crashes.


# Important Terms

Recursive call → When a function calls itself.

Base case → Stopping condition (so recursion doesn’t go forever).

Call stack → Python remembers each function call in memory (like a stack of plates ).

=======================================================================================================

# Decorators, Generators, Iterators

# What is Iterator?
-> An iterator is an object that allows you to go through (loop) elements one by one.

In Python, lists, tuples, and strings can all be made into iterators.

Syntax & Example
numbers = [1, 2, 3]
it = iter(numbers)      # create iterator

print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# print(next(it)) #  Error (no more items)

- Key functions:
iter() → makes an iterator
next() → gets next element

Normally we don’t call next() directly — we use a for loop (it calls next() internally).

for num in numbers:
    print(num)

-----------------------------------------------------------------------------------------------------

# What is Generator?
-> A generator is a special type of iterator.

Instead of storing all values in memory, it generates values one by one when needed.

Uses yield keyword instead of return.

Syntax & Example
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))   # 1
print(next(gen))   # 2
print(next(gen))   # 3


Generator is memory efficient because it doesn’t store all values at once.

Example: Squares
def squares(n):
    for i in range(1, n+1):
        yield i*i

for value in squares(5):
    print(value)


Output:
1
4
9
16
25 

---------------------------------------------------------------------------------------------------
# What is Decorator?
-> A decorator is a function that adds extra features to another function without changing its code.

Uses @ symbol in Python.

Syntax & Example
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello Students!")

say_hello()


Output:
Before function call
Hello Students!
After function call


Here:
decorator takes a function and adds extra behavior (before & after).

@decorator is just a shortcut for:

say_hello = decorator(say_hello)

------------------------------------------------------------------------------------

- Quick Summary
Concept	            What it is	                       Keyword/Method	Example
Iterator	Lets you loop through elements one by one	iter(), next()	for x in list:
Generator	Creates values one by one (saves memory)	yield	        Fibonacci, squares
Decorator	Adds extra functionality to a function	  @decorator	    Logging, auth check
