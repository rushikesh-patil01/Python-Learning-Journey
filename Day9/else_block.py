# WAP to demonstrate the use of else block in exception handling.

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")