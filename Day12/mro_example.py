# WAP to demonstrate Method Resolution Order (MRO).

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())