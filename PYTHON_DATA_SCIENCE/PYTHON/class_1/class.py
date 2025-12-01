class Car : 
    # Constructor 
    def __init__(self,tyres,windows,seats,type) :
        self.tyres = tyres
        self.windows = windows
        self.seats = seats
        self.type=type

    def car_self(self) : 
        print("the tyres inside  the car 1 is : {}".format(self.windows))
        print("the windows insdie the car 2 is {}".format(self.tyres))
        
    def car_self2(self):
        print("The windows inside the self car 2 is {}".format(self.tyres))
        print("the tyres inside the self car 2 is {}".format(self.windows))

    def car_electric(self,type):
        type = type 
        print("The type of car3 is {}".format(type))
        print("the number of tyres in car 3 is {}".format(self.tyres))



car1=Car(4,6,12,'Petrol')
car2=Car(5,8,14,'Diesel')
car3= Car(3,4,5,'Electric')
# print(car1.getcar1())
print(car1.tyres)
print(car1.windows)
print(car1.seats)   
car1.car_self()
car2.car_self2()
car3.car_electric('Electric')

# car3=Car("electric")
# print(car1.getCar1())