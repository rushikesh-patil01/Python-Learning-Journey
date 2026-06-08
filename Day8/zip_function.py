# WAP to Use zip()

names = ["Rahul", "Priya", "Amit"]
marks = [85, 92, 78]

for n, m in zip(names, marks):
    print(n, m)
    
    

# If lists have different lengths, zip() stops at the shortest list.

a = [1, 2, 3]
b = [10, 20]

print(list(zip(a, b)))