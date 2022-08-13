#overloading concept
class Book:
    def __init__(self,page):
        self.page=page
    def __add__(self,other):
        return self.page+other.page
b_one=Book(50)
b_two=Book(60)
add_book=b_one+b_two
print(add_book)
