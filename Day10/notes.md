# 

# File Handling-
File-A file is a named location on a storage device (like hard disk, SSD, or USB) that is used to store data permanently.

Unlike variables (which store data temporarily in RAM), files store data in secondary storage so it is not lost after the program ends.

Files can contain text, numbers, images, videos, or any type of data.

# Q1. What is file Handling?
-> File Handling in Python refers to the process of creating, reading, writing, updating, and deleting files using built-in functions.

Python provides the open() function and file objects to interact with files.

# Q2. Why File Handling?
-> To store data permanently (data in variables is temporary, but files are persistent).
To share data across programs.
Used in databases, logs, configurations, reports, etc.

# Q3. Why Do We Use File Handling?
-> We use File Handling to:

- Store data permanently
- Share data across programs
- Save reports and logs
- Manage large amounts of data


# Q4. What are File Modes in Python?
Mode	Meaning
"r"	   Read (file must exist)
"w"	   Write (creates new or overwrites existing file)
"a"	   Append (creates new or adds to existing file)
"x"	   Create (error if file exists)
"r+"   Read + Write
"b"	   Binary mode (e.g., "rb")

# 1.What is Create Mode (x)?
-> Create mode creates a new file and throws an error if the file already exists.
Syntax
open("filename.txt", "w")

# 2. What is Write Mode (w)?
-> Write mode is used to create a new file or overwrite an existing file.
file = open("myfile.txt", "w")
file.write("Hello, this is my first file.\n")
file.close()

# 3. What is Read Mode (r)?
-> Read mode is used to read data from an existing file.
Syntax
open("filename.txt", "r")

Code
file = open("myfile.txt", "r")
content = file.read()
print(content)
file.close()

# 4. Methods for reading:
read() → whole content

readline() → one line

readlines() → list of lines

# 5. What is Append Mode (a)?
-> Append mode adds data at the end of an existing file.

Example:

file = open("myfile.txt", "a")

# Q5. What is open() Function?
-> The open() function is used to open a file.
Syntax
file = open("filename.txt", "mode")

"filename.txt" → Name of the file

"mode" → Mode in which to open the file


# Q6. Insert into a File
-> Python files don’t have a direct insert feature (like arrays).
We usually:

Read file content.

Modify it in Python.

Write back.

Code (insert a line at top)

# Insert a line into file
with open("myfile.txt", "r") as file:
    lines = file.readlines()

lines.insert(0, "Inserted line at the top!\n")

with open("myfile.txt", "w") as file:
    file.writelines(lines)


# Q7.Pop (Remove) from a File
-> Similar logic: read → modify → write back.

Code (remove 2nd line)
with open("myfile.txt", "r") as file:
    lines = file.readlines()

# pop 2nd line (index 1)
lines.pop(1)

with open("myfile.txt", "w") as file:
    file.writelines(lines)

# Q8.Context Manager (with keyword)
-> Instead of manually opening and closing files, use with.
It automatically closes the file even if an error occurs.

Syntax
with open("filename.txt", "mode") as f:
    # work with f

Code
with open("myfile.txt", "a") as file:
    file.write("This line is added using context manager.\n")
