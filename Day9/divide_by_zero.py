# WAP to handle divide-by-zero exception using user input.

try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print("Result =", a / b)

except ZeroDivisionError:
    print("Second number cannot be zero")