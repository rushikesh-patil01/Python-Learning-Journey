Day 3 - Loops in Python

# Q1] What is a Loop? 
-> A loop is a control structure in programming that repeats a block of code multiple times, as long as a given condition is true.
Imagine you want to do something again and again.

For example:
- You want to say “Hello” 5 times.

# Q2] Why Do We Use Loops?
-> Loops help us:Save time, Write less code, Do things faster and correctly.

- Without loops:
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

- With a loop:
for i in range(5):
    print("Hello")
Much easier!

# Q3] How Many Loops in Python?
Python mainly has two loops but we use them in 4 common ways:
1️. while loop
2️. for loop with range()
3️. for loop for a list (iterative)     
4️. Nested loop (loop inside loop)

# 1. while Loop
- What is it?
Repeat code while a condition is True.
If condition becomes False, it stops.

syntax:
while condition:
    # code to repeat

- WAP TO Print numbers 1 to 5
- How it works:

Start: num = 1
Check: is num <= 5?
Yes → print it → add 1
Repeat until num is 6.

- Use while when:
You don’t know exactly how many times it will repeat. You stop when a condition is met.

# 2.for Loop with range()
- What is it?
Repeat code a fixed number of times.    

Syntax
for i in range(start, stop, step):

e.g. -range(6)#0 1 2 3 4 5
e.g.- range(1,11)#1 2 3 4 5 6 7 8 9 10
e.g. -range(2 ,11,2)#2 4 6 8 10

# code to repeat
start → where to begin (default: 0)   1:5 
stop → where to stop (not included!)
step → how much to increase (default: 1)

# 3.for Loop for Iterating a List     
- What is it?
Repeat code for every item in a list (or string).

Syntax
for item in list_name:
    # code to repeat

l=["banana","mango","Graps"]

l=[1]

- Use for for iteration when:
You want to check or do something for every item in a group.

# 4.Nested Loops
What is it?
A loop inside another loop.
Used for lists inside lists.

Syntax
for outer in outer_list:

    for inner in outer:
        # code to repeat

for  i  in range(3)  # outer loop     r= 0    c=0   
	for j in range(2)# inner loop 
		print(i,j)

- Real-life connection
You have boxes → inside boxes are gifts → open each box → take each gift:

boxes = [
    ["Toy", "Doll"],
    ["Puzzle", "Book"],
    ["Ball"]
]

for box in boxes:
    for gift in box:
        print("Found:",gift)

- Use nested loops when:
You have groups inside groups (rows & columns, boxes & items).

# Important: Avoid Infinite Loops
If the condition never becomes False → loop runs forever!

while True:
    print("Oops!")  # infinite loop
So always update your loop variable!

Why Loops Matter
 Save time
Write less code
 Make programs smarter
 Repeat tasks easily

# Q4] Difference Between for Loop and while Loop?
- for Loop : Used when the number of iterations is known. Easier to use with sequences.
- while Loop : Used when the number of iterations is unknown. Runs until a condition becomes False.

# Q5] What is range() Function?
-> The range() function generates a sequence of numbers.

Example: range(1, 11)

# Q6] What are the parameters of range()?

-> range() can take three parameters: range(start, stop, step)

Example: range(1, 10, 2)

# Q7] What is an Infinite Loop?
-> A loop that never ends because its condition always remains True.

Example:
while True:
    print("Hello")

# Q8] What is break Statement?
-> The break statement immediately terminates the loop.

# Q9] What is continue Statement?
-> The continue statement skips the current iteration and moves to the next iteration.

# Q10] What is pass Statement?
-> The pass statement is a null statement. It does nothing and acts as a placeholder.

# Q11] What are Loop Control Statements?
-> Loop control statements alter the normal execution of loops.
Examples:
break
continue
pass

# Q12] What is a Nested Loop?
-> A nested loop is a loop inside another loop.

# Q13] What is the use of loops in real-life programming?
-> Loops are used for:
Processing data
Reading files
Database operations
Automation
Repeating calculations

# 14] Which loop is more commonly used in Python?
-> The for loop is more commonly used because it is simple and works well with sequences like lists, tuples, strings, and ranges.

# 15] What is the advantage of using loops?
-> Loops reduce code duplication, improve readability, and save development time.
