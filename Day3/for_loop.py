# WAP Print numbers 1 to 5

for i in range(1,6):
    print(i)

# WAP print 1 to 10 even numbers using a loop
for i in range(2,11,2):
    print(i)


# print odd numbers using a loop
for i in range(1,11,2):
    print(i)
        
# WAP to print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)
        
# Clap your hands 5 times:
for i in range(5):
    print("clap")
        
# WAP to print the multiplication table of a given number.
num = int(input("Enter a number:"))
for i in range(1,11):
    print(num, "x",i,"=",num*i)
        
# WAP to Find Sum of First N Numbers
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i
print("Sum =", sum)

