# WAP to use Context Manager (with open) for file handling.
with open("myfile.txt", "a") as file:

    file.write("\nThis line is added using context manager.")

print("File Updated Successfully")