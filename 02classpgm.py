class Student:
    school_name="GGHSS"
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def disp_data(self):
        my_city="Calicut"
        print(f"my city is",my_city)
        print("school is",self.school_name)
name=input("enter your name")
city=input("enter your city")
s_one=Student(name,city)
s_one.disp_data()
print(s_one.__dict__)
print(Student.__dict__)
