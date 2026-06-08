# WAP to Use sorted() Function

names = ["Rahul", "Priya", "Amit"]
sorted_names = sorted(names, key=lambda n: len(n))
print(sorted_names)   # ['Amit', 'Rahul', 'Priya']