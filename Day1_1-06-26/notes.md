# Q1] What is the History of Python?
-> Python was created by Guido van Rossum and first released in 1991. It was designed to be simple, readable, and easy to learn.

----------------------------------------------------------------------------------------------------------------------------------

# Q2] What is Python?
-> Python is a high-level, interpreted, general-purpose programming language. It is easy to learn and widely used in web development, data science, automationn, AI and more.

---------------------------------------------------------------------------------------------------------------------------

# Q3] Features of python
-> Easy to Learn	Simple words, no curly braces {}
Interpreted	Runs line-by-line (like reading a book)
Dynamically Typed	No need to say "this is a number"
High-Level	Close to human language
Object-Oriented	Use classes and objects if needed
Portable	One code works everywhere
Huge Libraries	Pre-made tools for math, AI, games, etc.

----------------------------------------------------------------------------------------------------------------------------

# Q4] Variables in Python
-> A variable is a name used to store data in memory. In Python, variables are created automatically when a value is assigned to them. The `=` symbol is called the assignment operator. It is used to assign a value to a variable.
a = 10
b = 20
print(a+b) # 30

# Types of Variables in Python
1. Local Variable : Declared inside a function. Only works within that function.
2. Global Variable : Declared outside all functions. Can be accessed anywhere in the program.

---------------------------------------------------------------------------------------------------------------------------

# Q5] Data Types in Python 
-> To store different kinds of information properly.

1.Numeric Types (int, float, complex)
2.String Type (str)
3.Sequence Types (list, tuple, range)
4.Mapping Type (dict)
5.Set Types (set)
6.Boolean Type (bool)
------------------------------------------------

## 1. Numeric Types
# a. int — Integer
Stores whole numbers (positive or negative) without decimal point.

#Example: Age, number of students, marks (whole number).
a = 3

# b. float — Floating-point Number
Stores decimal numbers.

Example: Height, weight, price.
pi = 3.14
price = 99.99

# c. complex — Complex Number
Stores a number with real + imaginary parts.
Mostly used in scientific calculations.

Example:
z = 2 + 3j   # 2 is real, 3j is imaginary
a = 3 + 3j
--------------------------------------------------
# 2. String Type
str — String
Stores text (a sequence of characters).

Example: Names, messages, sentences.
name = "Rushikesh"
message = 'Hello World!'
You can join, split, slice strings.
---------------------------------------------------
## 3. Sequence Types
Used to store multiple items in order.

# a) list — List
Stores many items in one variable.
Ordered & mutable (you can change items).
Can hold mixed data types.

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"   # Change banana to orange
print(fruits(1))

# b) tuple — Tuple
Like a list, but cannot change (immutable).
Faster & safe for fixed data.

point = (10, 20,"Raj",10.5)
# point[0] = 5  # Error: Tuples cannot be changed

# c) range — Range  - immutable
Creates a sequence of numbers.
Mostly used in loops.
Syntax - range(Start, end, increment)

odd  number 11 
nums = range(1 11 2 ) # o/p:1 3 5 7 9 

for i in range(3):
    print(i) 
----------------------------------------------------------------

## 4.Mapping Type
dict — Dictionary
Stores data as key-value pairs.
Used when you want to label your data.

student = {
    "name": "Rushi",
    "age": 20
}

print(student["name"])   # Rushi
student["age"]           # 22
student["age"] = 21      # Change value
------------------------------------------------------------

## 5.Set Types
Used to store unique, unordered items.
set — Set
Stores unique items (no duplicates).
Unordered — items may appear in any order.

Mutable — you can add/remove items.

s = {1, 2, 3, 2, 1}
print(s)   # {1, 2, 3}  (duplicates removed)
s.add(4)
-------------------------------------------------------------

# 6.Boolean Type
bool — Boolean
Stores True or False.

Mostly used in conditions and comparisons.
is_valid = True
is_done = False
=================================================================================================================================
