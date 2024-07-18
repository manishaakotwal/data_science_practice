#class attributes- instance variable & class variable
''' 
instance variable- declare in __init__()
access and modified by dot notation.
class variable- declare in outside the methd but within the class
access by class name

'''
class Student():
    #class variable
    school_name = "ABC"
    #instance variable
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1 = Student("jessa",22)
#access instance variable
print("Student", s1.name, "age:",s1.age)

#access class variable
print("school name:", Student.school_name)

# modifying the instance variable
s1.name="john"
s1.age=15
print("student_detail:" ,s1.name,s1.age)

#modifying the class variable
Student.school_name="kalpvraksh"
print("school name:",Student.school_name)


