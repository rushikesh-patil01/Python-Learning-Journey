# WAP to manually raise an exception using the raise keyword.

age = int(input("Enter Age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Eligible")