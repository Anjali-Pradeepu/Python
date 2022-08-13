import usrdefinedexcpt.py
age=int(input("Enter your age"))
if age<18:
    raise TooYoungException("Young")             #raise is used to call exception
elif age>18 and age<=60:
    raise TooOldException("old")
else:
    print("Mail")
