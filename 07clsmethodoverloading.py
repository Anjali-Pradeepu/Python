#method overloading checking (but there is no concept like in python)
def add(x,y):
    return x+y
def add(x,y,z):
    return x+y+z
print(add(2,3))    # the last method will get working and returning error saying there is no third argument
