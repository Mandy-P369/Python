class Animal : 
    def __init__(self,*args):
        if len(args)==1:
            self.name=args[0]
        elif len(args)==2:
            self.name = args[0]
            self.species = args[1]
        elif len(args)==3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    def makesound(self,sound):
        sound=sound 
        return "Tha animal name is lion and says {} ".format(sound)
    

dog = Animal("Tommy","Bark",15)
dog.makesound('roar')
print(dog)
print(dog.name)
print(dog.species)
print(dog.age)

class Culture: 
    def __init__(self,state,country):
        self.state= state
        self.country = country
    def details (self):
        print(self.state)
        print(self.country)
culture = Culture('UP','India')
culture.details()


        
