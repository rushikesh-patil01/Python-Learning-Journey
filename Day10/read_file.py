# 1. WAP to read the complete content of a file.

file = open("myfile.txt", "r")

content = file.read()

print(content)

file.close()


# 2. WAP to read only one line from a file.

file = open("myfile.txt", "r")

print(file.readline())

file.close()