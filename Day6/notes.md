# Day 6 - Tuple, Set and Dictionary in Python

# Q1. What is a Tuple in Python?
-> A tuple is an ordered and immutable collection of elements enclosed in parentheses ().

Example:
numbers = (10, 20, 30)

# Q2. Is Tuple Mutable or Immutable?
-> Tuple is immutable, meaning its elements cannot be modified after creation.

Example:
numbers = (10, 20, 30)
-  numbers[0] = 100  # Error

# Q3. What is Tuple Indexing?
-> Tuple indexing is used to access elements using their position.

# Q4. What are Tuple Methods?
-> Tuple has only two built-in methods:

count()
index()

# Q5. What is Tuple Packing and Unpacking?

- Packing: data = 10, 20, 30

- Unpacking: a, b, c = (10, 20, 30)
  print(a, b, c)


# SET
# Q6. What is a Set in Python?
-> A set is an unordered collection of unique elements enclosed in curly braces {}.

Example:
numbers = {10, 20, 30}

# Q7. Why are Sets Used?
-> Sets are used to store unique values and remove duplicates.

Example:
numbers = {10, 20, 20, 30}
print(numbers)

Output: {10, 20, 30}

# Q8. What are Set Methods?
-> Common Set Methods:

add()
remove()
discard()
pop()
clear()

# Q9. What is Union in Set?
-> Union combines all unique elements from two sets.

Example:
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
output : {1, 2, 3, 4, 5}

# Q10. What is Intersection in Set?
-> Intersection returns common elements from two sets.

Example:
A = {1, 2, 3}
B = {3, 4, 5}

print(A.intersection(B))

output : {3}

# Dictionary

# Q11. What is a Dictionary in Python?
-> A dictionary stores data in key-value pairs.

# Q12. Is Dictionary Mutable or Immutable?
-> Dictionary is mutable, meaning values can be changed after creation.

Example:
student = {
    "name": "Rushikesh"
}

student["name"] = "Rushi"

# Q13. What are Dictionary Methods?
keys()
values()
items()
get()
update()
pop()

Example:
student = {
    "name": "Rushikesh",
    "age": 22
}

print(student.keys())
print(student.values())

output :
keys : 'name', 'age'
values : 'Rushikesh', 22

# 

| Data Structure | Syntax        | Ordered | Mutable | Duplicates       |
| -------------- | ------------- | ------- | ------- | ---------------- |
| List       | `[]`          | Yes     | Yes     | Allowed          |
| Tuple    | `()`          | Yes     | No      | Allowed          |
| Set      | `{}`          | No      | Yes     | Not Allowed      |
| Dictionary | `{key:value}` | Yes     | Yes     | Keys Not Allowed |
