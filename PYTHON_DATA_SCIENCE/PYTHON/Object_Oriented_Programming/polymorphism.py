# Polymorphism :  When the same operator  is allowed to  have the different meaning according to the
# context ....
print(1+5) #6
print("aayush" + "pateriya") # aayushpateriya
print([1,3,4]+[7,8,9]) # merge 


class Complex : 
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def shownumber(self) : 
            print(self.real,"i +",self.img,"j")

    def add(self,num2):
         newreal = self.real + num2.real
         newimg = self.img + num2.img
         return Complex(newreal,newimg)
    
    def __add__(self,num2) : 
         newreal = self.real + num2.real
         newimg = self.img  + num2.img
         return Complex(newreal,newimg)

real1 = int(input("Enter the real 1   : "))
img1 = int(input("Enter the img 1    :"))
num1 = Complex(real1,img1)
real2 = int(input("Enter the real 2   :"))
img2 = int(input("Enter the img   :"))
num2 = Complex(real2,img2)

num3 = num1 + num2
num3 = num1.add(num2)
print("------------------------------")
num3.shownumber()

         
    