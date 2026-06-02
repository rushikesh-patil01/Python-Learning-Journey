Day 2: Operators + Conditional Statements

# Q1] What are operators in Python?
-> Operators are symbols used to perform operations on variables and values.
Operators: Special symbols use to perform some operations

 a + b => + operator ; a,b operands; (a+b) operation

 Unary : perform operation on single operand (not) 
 Binary : perform operation on two operand (+,-,*,/,etc)

# Q2] Types of Operators?
-> 1- Arithmetic Operators  (+,-,*,/,%,//,**)
2- Assignments Operators (=,+=,-=,*=,/=,%=,//=,**=)
3- Comparsion Operators  (<,>,<=,>=,==,!=)
4- Logical Operators     (and , or , not)
5- Membership Operators  (in , not in)
6- Identity Operators    (is, is not)
7- Bitwise Operators      (&,|,~,^,<<,>>)

# Condition Statement
# Q3] What is Condition Statements?
-> Conditional statements allow a program to make decisions and execute specific blocks of code based on whether a condition is True or False.

# Q4] What are the types of conditional statements in Python?
->  1. if statement

    2. if-else statement

    3. if-elif-else

    4. Nested if-else statement

# 1. if statement
- The if statement checks a condition. If the condition is True, the block of code inside it runs. Otherwise, it does nothing.
Syntax:

if condition:
    # code block to execute

 Example:
age = 20
if age >= 18:
    print("You are eligible to vote.")

# 2. if-else Statement
- The if-else statement provides an alternative path. If the condition is True, the if block runs. If it is False, the else block runs.
Syntax:
if condition:
    # code block if true
else:
    # code block if false
 Example:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. if-elif-else Statement
- Use this when there are multiple conditions. The first if that evaluates to True is executed. If none match, the else block is executed (optional).
Syntax:
if condition1:
    # block1
elif condition2:
    # block2
elif condition3:
    # block3
else:
    # default block

Example:
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# 4. Nested if-else Statement
- A nested if is an if or else block inside another if or else block. Useful for multi-level decisions.
Syntax:
if condition1:
    if condition2:
        # nested block
    else:
        # nested else block
else:
    # outer else block

Example:

age = int(input("Enter your age: "))
if age >= 18:
    citizen = input("Are you an Indian citizen? (yes/no): ")
    if citizen.lower() == "yes":
        print("Eligible to vote in India.")
    else:
        print("Not eligible to vote in India.")
else:
    print("You are underage.")


# Summary Table
Statement Type	  Use Case
if	              To check one condition only
if-else	          To choose between two paths
if-elif-else	  To handle multiple conditions
Nested if-else	  For multi-level conditional logic

# Q5] What is an if Statement?
-> The if statement executes a block of code only when the given condition is True.

# Q6] Difference Between if and if-else?
-> if:
Checks only one condition.
Executes code only when the condition is True.

-> if-else:
Provides two possible outcomes.
Executes one block when True and another when False.

# Q7] Difference Between Comparison and Logical Operators?
Comparison Operators
-> Used to compare two values.

Examples:
==
!=
>
<
>=
<=
Logical Operators
-> Used to combine multiple conditions.

Examples:
and
or
not



