# Swap two numbers
# Swapping means exchanging the values of two variables. 

a = 10
b = 20
a,b = b,a
print("a=",a)
print("b=",b)

# Swap using a temporary variable
temp = a    
a = b  
b = temp  

print("\nAfter swapping using a temporary variable:")
print("a =", a)
print("b =", b)