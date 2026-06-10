# WAP to remove the second line from a file.
with open("myfile.txt", "r") as file:
    lines = file.readlines()

lines.pop(1)

with open("myfile.txt", "w") as file:
    file.writelines(lines)

print("Line Removed Successfully")