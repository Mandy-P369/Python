# Class is the blue print for creating object ...
# class Student:
#     name = "aayush"
#     branch = "AI ML"

#     def __init_(self,name,branch):
#         self.name = name
#         self.branch = branch
    
#     def welcome(self):
#         print("Welcome student",self.name,'to the branch {}'.format(self.branch))

# name = input("Enter the name")
# branch = input("Enter the branch")
# st = Student()
# print(st.name)
# print(st.branch)
# st.welcome()


# init Functions inside the python :
# All classes have functions called __init__ , which is always execute when class is being initiated..
# Creating class                                      
# class Car :
#   def __init__(self,fullname):                                            
#      self.fullname = fullname
# 
# 
# Creating object : 
#   car = Car("mercedes benz")
#   print(car.fullname)
                                    
    
# class Car : 
#     def __init__(self,fullname):
#         self.fullname = fullname 

# car = Car("Maruti")
# print(car.fullname)

        

# Static method : 
# methods that don't use the self parameter (work at class level).
class Teacher : 
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    @staticmethod
    def institute(insname):
             print('he/she teach in {}',insname)
        

name = input("Enter the name of the teacher")
age = int(input("Enter the age of the teacher"))
teacher = Teacher(name,age)
teacher.institute('Xansa IT solutions')

# Decorator allow to wrap another function  in order to 
# extend the behaviour of the wrapped functions , without permanently 
# modifying it 

