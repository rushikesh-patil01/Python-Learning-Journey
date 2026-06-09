# Day 9 : Exception Handling in Python

# Q1. What is Exception Handling?
- An exception is an error that occurs during program execution.
- Without handling, the program stops abruptly.
- Exception Handling allows the program to catch and respond to errors gracefully.
- Common exceptions: ZeroDivisionError, IndexError, ValueError, FileNotFoundError, etc.

# Q2. Why Do We Use Exception Handling?
-> We use Exception Handling to:

- Prevent program crashes
- Handle errors gracefully
- Improve program reliability
- Provide meaningful error messages
- Continue program execution when possible


# Q3. What is Exception Hierarchy?
- Python exceptions are classes organized in a hierarchy.
- Key points:
    - BaseException → Top-most parent of all exceptions.
    - Exception → Most user-defined exceptions inherit from this.
    - Catch specific exceptions first, then general ones.

# Simplified hierarchy:

BaseException
│
├── SystemExit
├── KeyboardInterrupt
├── Exception
     ├── ArithmeticError
     │    ├── ZeroDivisionError
     │    └── OverflowError
     ├── LookupError
     │    ├── IndexError
     │    └── KeyError
     ├── ValueError
     ├── TypeError
     └── OSError
          ├── FileNotFoundError
          └── PermissionError

Tip: Never catch BaseException unless necessary; it includes system-level events.

# Techniques in Exception Handling
-> These are the main concepts or techniques used to handle exceptions:

- try-except → Handle exceptions that occur in a block of code.

- else → Execute code if no exception occurs.

- finally → Execute code regardless of whether an exception occurs.

- raise → Manually trigger an exception.

- Exception Hierarchy → Understanding which exceptions inherit from others to catch them correctly.

# Keywords and Syntax
Keyword	Purpose	Syntax
try	Code that may raise an exception	                try:\n # code that may raise exception
except	Handle the exception that occurs	            except ExceptionType:\n # handle exception
else	Runs only if no exception occurs in the try block	else:\n # runs if no exception occurs
finally	Always executes regardless of an exception	       finally:\n # always executes
raise	Manually raise an exception	raise ExceptionType("Error message")


#  Keywords in Exception Handling
# a) try-except
Theory:
- try → code that might raise an exception.
- except → handles the exception if it occurs.

Syntax:
try:
    # code that may raise exception
except ExceptionType:
    # code to handle exception

Example:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

Output:
Cannot divide by zero!


# b) else
Theory:
- Runs only if no exception occurs in the try block.

Syntax:
try:
    # code that may raise exception
except ExceptionType:
    # handle exception
else:
    # runs if no exception occurs

Example:
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")

Output:
Division successful!

# c) finally
Theory:
- Always executes regardless of an exception.
- Useful for cleanup tasks like closing files.

Syntax:
try:
    # code that may raise exception
except ExceptionType:
    # handle exception
finally:
    # always executes

Example:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always executes.")


# d) raise
Theory:
- Used to manually raise an exception.
- Useful for input validation or custom errors.

Syntax:
raise ExceptionType("Error message")

Example:
age = -5
if age < 0:
    raise ValueError("Age cannot be negative!")

Output:
ValueError: Age cannot be negative!

# Key Notes :

- Exception handling prevents program crashes.
- Use try-except to catch errors.
- Use else for code that runs if no errors occur.
- Use finally for cleanup tasks.
- Use raise to trigger custom exceptions.
- Catch specific exceptions first, then general ones (Exception).
- Avoid catching BaseException unless needed.


try_except.py
multiple_exceptions.py
else_block.py
finally_block.py
raise_exception.py
divide_by_zero.py
file_not_found.py
user_input_exception.py
custom_exception.py