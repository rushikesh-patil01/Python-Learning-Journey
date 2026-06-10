# 1. WAP to write data into a file.

file = open("myfile.txt", "w")

file.write("Rushikesh Patil")

file.close()

print("Data Written Successfully")


# 2. WAP to append data into an existing file.
file = open("myfile.txt", "a")

file.write("\n Welcome ")

file.close()

print("Data Appended Successfully")