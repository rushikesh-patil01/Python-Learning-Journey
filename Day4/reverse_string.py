# WAP to Reverse a String

text = input("Enter a string: ")

print("Reverse =", text[::-1])

# # WAP to Reverse a String Using a Loop

text = input("Enter a string: ")

reverse = ""

for i in text:
    reverse = i + reverse

print("Reverse =", reverse)