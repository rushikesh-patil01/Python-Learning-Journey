'''
6- Identity Operators    (is, is not)
used to chek the memory location of two object

is =return true  if two varibale point to the same objects in memory

a  is  b  true
a not is b=false

'''
a=[1,2,3]
b=[1,2,3]
c=a

print(a == b)  # check the content is same or not
print(a is b)  # check that 2 datatypes are same object or not
print(c is a)  # True
print(a is c)  # True

print(id(a))
print(id(b))
print(id(c))

'''
address of a and c is same
while address of a and b are different
'''

print(a is not b) # True 
print(c is not a) # False
print(a is not c) # False