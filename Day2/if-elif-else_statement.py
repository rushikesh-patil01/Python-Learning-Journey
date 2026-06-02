# WAP to Calculate Grade Based on Marks.
marks = eval(input("Enter a marks :"))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# WAP check Classify age group (child, teenager, adult, senior).
age = int(input("Enter your Age:"))
if age<=12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# WAP Find the largest of three numbers.
a = int(input("Enter a number_1 :"))
b = int(input("Enter a number_2 :"))
c = int(input("Enter a number_3 :"))
if a >= b and a >= c:
    print(a, "a is a largest number")
elif b >= a or b >=c :
    print(b,"b is a largest number")
else:
    print(c, "c is a largest number")


