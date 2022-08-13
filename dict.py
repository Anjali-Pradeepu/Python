person_info={"name":"Tony",
             "age":22,
             "salary":40000,
             "city":"Bangalore"}
print(person_info)
for key,value in person_info.items():
    print(key,value,sep="-")
person_info.pop("age")
print(person_info)
person_info.popitem()
print(person_info)
