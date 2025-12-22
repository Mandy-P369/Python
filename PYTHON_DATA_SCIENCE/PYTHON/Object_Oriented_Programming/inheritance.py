# Inheritance : When one class  (child/derived) derives the properties and methods of another class(parent/base)...
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car start")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__(self,name):
        self.name = name 

car1 = Toyota("Fortuner") 
car2 = Toyota("prius")
print(car1.name)

print(car2.start())
print(car2.stop())
print(car2.color)