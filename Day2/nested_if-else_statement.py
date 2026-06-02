# WAP to Check Voting Eligibility Based on Age and Citizenship

age = int(input("Enter your age: "))
if age >= 18:
    citizen = input("Are you an Indian citizen? (yes/no): ")
    if citizen.lower() == "yes":
        print("Eligible to vote in India.")
    else:
        print("Not eligible to vote in India.")
else:
    print("You are underage.")
    
# WAP Check driving license eligibility (age and eyesight)
age = int(input("Enter your age: "))

if age >= 18:
    eyesight = input("Is your eyesight good? (yes/no): ")

    if eyesight.lower() == "yes":
        print("Eligible for Driving License")
    else:
        print("Not Eligible due to poor eyesight")
else:
    print("Not Eligible due to age")
    
# WAP Verify login: first check username, then password.
username = input("Enter Username: ")

if username == "admin":
    password = input("Enter Password: ")

    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

