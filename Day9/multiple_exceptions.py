# WAP to handle multiple exceptions (ValueError and ZeroDivisionError)

try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot divide by zero")