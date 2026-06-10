# WAP to handle FileNotFoundError.

try:

    file = open("myfile.txt", "r")

    print(file.read())

except FileNotFoundError:

    print("File Not Found")