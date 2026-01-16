class Car:
    color = "black"
    @staticmethod
    def start() : 
        print("The car start")

class Car2 : 
    @staticmethod
    def stop():
        print("The Car stopped")

class Toyota(Car,Car2):
    def __init__(self,name):
        self.name = name
        print("The name of the car is ",name)
        Car.start()
        Car2.stop()
    

toy=Toyota("Fortuner")
print(toy)


# Super method : Super method is the method used to access the methods of the parent class .....
 