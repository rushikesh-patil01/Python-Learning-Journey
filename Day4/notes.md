# Day 4 - Strings in Python

# Q1. What is a String in Python?
-> A string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''').

- Example:
name = "Rushikesh"

# Q2. Is String Mutable or Immutable?
-> Strings are immutable, which means once a string is created, its content cannot be changed.

Example:
name = "Python"
# name[0] = "J"  -- Error

# Q3. What is String Indexing?
-> String indexing is used to access individual characters of a string using their position number.

Example:
text = "Python"
print(text[0]) --# P

# Q4. What is String Slicing?
-> String slicing is used to extract a part of a string.

Example:
text = "Python"
print(text[0:3]) # --Pyt

## Q5. Difference Between Indexing and Slicing?

 Indexing                    | Slicing                      
 
 Accesses a single character | Accesses multiple characters 
 Returns one value           | Returns a substring          
 Example: text[0]            | Example: text[0:3]           


# Q6. What is len() Function?
-> The `len()` function returns the total number of characters in a string.

Example:
text = "Python"
print(len(text)) # 6


# Q7. What are String Methods?
-> String methods are built-in functions used to perform operations on strings.

- Common Methods:

* upper()
* lower()
* title()
* replace()
* split()
* strip()
* count()
* find()

- Example:
text = "python"
print(text.upper())

# Q8. What is String Concatenation?
-> String concatenation means joining two or more strings using the `+` operator.

Example:
first = "Hello"
second = "World"

print(first + " " + second) --# Hello World


# Q9. What is String Traversal?
-> String traversal means accessing each character of a string one by one using a loop.

Example:
text = "Python"

for ch in text:
    print(ch)


# Q10. How to Reverse a String?
-> A string can be reversed using slicing.

text = "Python"
print(text[::-1]) --#nohtyP


# Q11. How to Check a Palindrome String?
-> A string is a palindrome if it reads the same forward and backward.

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

Example:
madam → Palindrome
python → Not Palindrome

