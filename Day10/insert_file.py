# WAP to insert a line at the beginning of a file.
with open("myfile.txt", "r") as file:
    lines = file.readlines()

lines.insert(0, "My name is Rushikesh!\n")

with open("myfile.txt", "w") as file:
    file.writelines(lines)

print("Line Inserted Successfully")