#static class
class CustomMath:
    @staticmethod
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
print(CustomMath.add(100,200))
print(CustomMath.sub(200,100))
