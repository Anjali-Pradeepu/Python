#To call particular super class method
class A:
    def m1(self):
        print("A class Method")
        print(id(self))
class B(A):
    def m1(self):
        print("C class Method")
class C(B):
    def m1(self):
        print("C class Method")
class D(C):
    def m1(self):
        print("D class Method")
class E(D):
    def m1(self):
        A.m1(self)
        print(id(self))
e=E()
e.m1()
