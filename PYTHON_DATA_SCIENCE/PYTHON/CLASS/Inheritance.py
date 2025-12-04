class Car: 
    def __init__(self, windows, doors, enginetype):
        self.windows = int(windows)
        self.doors = int(doors)
        self.enginetype = enginetype
        self.amount = 0
        self.tax = 0
    
    def driving(self):
        print(f"This is a self-driving car with {self.doors} doors, {self.windows} windows and a {self.enginetype} engine.")

    def costofcar(self, *args):
        if len(args) == 1:
            self.enginetype = args[0]
        elif len(args) == 2:
            self.enginetype = args[0]
            self.amount = int(args[1])
        elif len(args) == 3:
            self.enginetype = args[0]
            self.amount = int(args[1])
            self.tax = int(args[2])

        return self.enginetype, self.amount, self.tax
        
    def calculation(self):
        print("Tax on the car:", self.tax)
        print("Amount of the car:", self.amount)
        print("Engine type:", self.enginetype)
        
        finalprice = self.amount + (self.amount * self.tax) / 100
        print("Final price of the car is:", finalprice)

class Audi(Car):
     def __init__(self, windows, doors, enginetype, horsepower): 
          self.horsepower = horsepower
          super().__init__(windows, doors, enginetype)
          print("Windows in Audi:", self.windows)
          print("Speed / HP:", horsepower)
          print("Doors in Audi:", self.doors)



tax = int(input("Enter tax: "))
amount = int(input("Enter amount: "))
enginetype = input("Enter engine type: ")

car = Car(4, 5, enginetype)   # Correct values
car.costofcar(enginetype, amount, tax)
car.driving()
car.calculation()

print("--------------------------------")

audi = Audi(4, 5, 'petrol', 50)
audi.costofcar('petrol', 600000, 12)
audi.calculation()

print("---------------------------------")
