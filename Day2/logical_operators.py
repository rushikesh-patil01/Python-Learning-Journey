# 4- Logical Operators     (and , or , not)

'''
# 1-and
T and T = T
T and F = F
F and T = F
F and F = F

# 2-or
T or T = T
T or F = T
F or T = T
F or F = F

# 3-not
not T = F
not F = T

'''
a=5
b=3
print((a>b) and (a==5)) # T and T = T
print((a>b) and (a!=5)) # T and F = F
print((a<b) and (a==5)) # F and T = F
print((a<b) and (a!=5)) # F and F = F

a=5
b=3
print((a>b) or (a==5)) # T or T = T
print((a>b) or (a!=5)) # T or F = T
print((a<b) or (a==5)) # F or T = T
print((a<b) or (a!=5)) # F or F = F

a=5
b=3
print(not(a>b))  # not(T) = F
print(not(a!=5)) # not(F) = T

print(not((a>b) and (a==5))) #not( T and T) = not(T)=F
print(not((a>b) and (a!=5))) #not( T and F) = not(F)=T
print(not((a<b) and (a==5))) #not( F and T) = not(F)=T
print(not((a<b) and (a!=5))) #not( F and F) = not(F)=T

print(not((a>b) or (a==5))) #not( T or T) = not(T)=F
print(not((a>b) or (a!=5))) #not( T or F) = not(T)=F
print(not((a<b) or (a==5))) #not( F or T) = not(T)=F
print(not((a<b) or (a!=5))) #not( F or F) = not(F)=T