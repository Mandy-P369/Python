# Define a circle  to create a circle with radius r using the constructor ....
# Define the Area() method  of the class  which calculates the area of the circle ...
# Define the parameter() method  of the class  which allows us to calculate the perimeter of circle ...
import math
class Circle : 
    def __init__(self,radius):
        self.radius = radius 
        self.area = math.pi*self.radius 
        self.area 
    
    @property
    def changeradius(self) : 
        print("The new radius of the circle is : {}".format(self.radius))
        area = math.pi*self.radius
        return area 
    
radius = int(input("Enter the radius of the circle"))
circle = Circle(radius)
print(circle.area)