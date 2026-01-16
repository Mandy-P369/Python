class Car :
    pass
car1 = Car()
car2 = Car()

car1.engine = 'Diesel engine'
car2.engine = 'Petrol Engine'

car1.windows = 4
car2.windows = 6

print(car1.engine)
print(car2.engine)
print(car1.windows)
print(car2.windows)
car3 = Car()


print(dir(car2)) ## Show the methods visible in this object ..
# def car(*args,**kwargs):
#     print("The engine used in car1 is "+ args)
#     print("the windows exist in car2 are"+kwargs)

# car3.model= car(car2.windows,engines = car1.engine)
    




    