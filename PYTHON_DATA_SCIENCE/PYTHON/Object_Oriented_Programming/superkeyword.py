class Car:
    def __init__(self,type):
        self.type= type
    
    @staticmethod
    def start():
        print("The car start")
    
    @staticmethod
    def stop():
        print("The car stop")

class Tata(Car):
    print("This is the next class inherit the property of the Car class")
    def __init__(self,name,type):
        self.name = name  
        super().__init__(type)
        super().start()

car = Tata("Maruti","CNG")
print(car.type)
car2 = Car("Diesel")
print(car2.type)
print(car.type)

        

