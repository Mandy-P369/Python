# del keyword :
# Used to delete object properties  and object itself .
 

# # Private(like) attributes and methods :
# Private  attributes and methods are  meant to be used inside only within the class and are not
# accessible from the outside of the class 
# class Student: 
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age 

#     def student_age(self):
#         print("The age of the student is : {}".format(self.__age))

# name= input("Enter the name of the student")
# age= input("Enter the age of the student")
 
# student = Student(name,age)
# print(student.name)
# print(student.student_age())

class Person: 
    __name = "aayush "

    def __hello(self): 
        print("Hello Aayush !, I am from Lalitpur")

    def __welcome(self): 
        self.__hello()
        print("This is the private welcome method .")

    def call(self):
        self.__welcome()


person = Person()
# print(person.__hello())
# print(person.__name)
person.call()




        