# Property decorator ..... 
# We use property decorator on any method  in the class to use the method as a property ...

class Student : 
    def __init__(self,phy,maths,chem):
        self.phy = phy 
        self.maths = maths
        self.chem = chem
        self.percentage = (self.phy+self.chem+self.maths)/3 

    @property 
    def percentage_obtain(self) : 
        print("physics marks : {} , chemistry marks : {} , mathsmarks : {}".format(self.phy,self.chem))
        return str((self.phy + self.chem + self.maths)/3) + "%"
    

phy = int(input("Enter the physics marks"))
chem = int(input("Enter the chemistry marks "))
maths = int(input("Enter the mathematics marks "))

student = Student(phy,chem,maths)
print(student.percentage_obtain)

phychange = int(input("Enter the physics imporoved marks"))
student.phy = phychange 
chemchange = int(input("Enter the chemistry imporoved marks"))
student.chem = chemchange
mathschange = int(input("Enter the maths imporoved marks "))
student.maths = mathschange
print(student.percentage_obtain)
