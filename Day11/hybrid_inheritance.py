class A:
    def displayA(self):
        print("Class A")

class B(A):
    def displayB(self):
        print("Class B")

class C:
    def displayC(self):
        print("Class C")

class D(B, C):   # Hybrid (Multilevel + Multiple)
    def displayD(self):
        print("Class D")

d1 = D()
d1.displayA()
d1.displayB()
d1.displayC()
d1.displayD()