# Day 5 - Lists in Python

# Q1. What is a List in Python?
-> A list is an ordered and mutable collection used to store multiple items in a single variable.

Example:
numbers = [10, 20, 30, 40]
print(numbers)

# Q2. Is List Mutable or Immutable?
-> Lists are mutable, which means their elements can be modified after creation.

Example:
numbers = [10, 20, 30]
numbers[0] = 100
print(numbers)

Output:[100, 20, 30]

# Q3. What is List Indexing?
-> List indexing is used to access individual elements using their position.

Example:
numbers = [10, 20, 30, 40]
print(numbers[0])

Output: 10

# Q4. What is List Slicing?
-> List slicing is used to extract a portion of a list.

Example:
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

Output: [20, 30, 40]

# Q5. What is List Traversal?
-> List traversal means accessing each element of a list one by one using a loop.

Example:
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

# Q6. What is len() Function?
-> The len() function returns the total number of elements in a list.

Example:
numbers = [10, 20, 30, 40]
print(len(numbers))  # 4

# Q8. What are List Methods?
-> List methods are built-in functions used to perform operations on lists.

- Common List Methods
- append()
- insert()
- remove()
- pop()
- sort()
- reverse()
- count()
- index()

# Q9. What is append() Method?
-> The append() method adds an element at the end of the list.

# Q10. What is insert() Method?
-> The insert() method adds an element at a specific position.

# Q11. What is remove() Method?
-> The remove() method removes a specific value from the list.

# Q12. What is pop() Method?
-> The pop() method removes an element using its index.

# Q13. Difference Between append() and insert()?
append()	         |    insert()
Adds element at end	 |    Adds element at specific position
Takes one argument	 |    Takes index and value

# Q14. Difference Between remove() and pop()?
remove()	       |    pop()
Removes by value   |     Removes by index
Value required	   |    Index required

