# Class method are the method which is bound  to the class and recieves the class as an implicit 
# first arguement .....
# Note : Static method can't  access  or modify class state  and generally  for utility .
class Person  : 
    name = "Aayush"
    def __init__(self,nature,gender):
        self.gender = gender
        self.nature = nature 

    @classmethod
    def changeName(cls,name) :
        cls.name = name

    @classmethod
    def changeNature(cls,nature ) :
        cls.nature = nature 

nature = input("Enter the nature to change ")
p = Person("warm","male")
p.changeName("Arjab")
print(p.name)
print(Person.name)
print(p.changeNature("nature"))
print(p.nature)



        