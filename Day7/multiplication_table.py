# WAP to print multiplication table using a function.

def table(num):
    for i in range(1, 11):
        print(num ,'x',i, '=', i * num)
        
table(2)