# WAP print number 1 to 5 in while loop

num = 1  # start
while num <= 5:   
    print(num)      
    num += 1
    
# WAP  Eat chocolates while you have them:
chocolates = 3

while chocolates > 0:
    print("Eat chocolate")
    chocolates -= 1
    
# WAP to Print Numbers from 5 to 1
num = 5
while num >= 1:
    print(num)
    num -= 1
    
# WAP to Print Even Numbers from 1 to 10
num = 2
while num <= 10:
    print(num)
    num += 2

# WAP to Print odd Numbers from 1 to 10
num = 1
while num <= 10:
    print(num)
    num += 2
    
# WAP to Find Sum of First N Natural Numbers
n = int(input("Enter a number: "))

num = 1
sum = 0
while num <= n:
    sum += num
    num += 1

print("Sum =", sum)
