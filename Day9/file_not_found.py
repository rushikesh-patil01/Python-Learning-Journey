# WAP to handle FileNotFoundError.

try:
    file = open("data.txt", "r")

except FileNotFoundError:
    print("File Not Found")