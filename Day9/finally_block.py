# WAP to demonstrate the use of finally block.

try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program Finished")