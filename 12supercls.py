#super class continues...
class P:
    def __init__(self):
        print("parent Constructor")
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent static method")
class C(P):
    @classmethod
    def m1(cls):
        #super().__init__()
        #super().m1()
        super().m2()
        super().m3()
#c=C()
C.m1()  #directly accessing method in the class
