class Student:
    school_name="GGHSS"
    def __init__(self):
        self.city="Bangalore"
    @classmethod
    def stud_data(cls,name):
        print("school name is ",cls.school_name)
        print("name of student is ",name)
print("city is ",self.city)
Student.stud_data("Mary")
