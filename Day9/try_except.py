# WAP to handle ZeroDivisionError using try-except.

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")