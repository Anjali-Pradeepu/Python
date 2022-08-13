#polymorphism concept
class Duck:
    def talk(self):
        print("Quack quack")
class Dog:
    def talk(self):
        print("Bow bow")
def obj_fun(obj):
    obj.talk()
d=Duck()
obj_fun(d)
dg=Dog()
obj_fun(dg)

