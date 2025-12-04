class BankAccount :
    SI=0
    net_change = 0
    # def __init__(self,principle,rate,time):
    #     self.principle = principle 
    #     self.rate = rate
    #     self.time = time
    
    def __init__(self,*args):
        interest = 0
        if len(args)==1:
            self.principle = args[0]
        elif len(args)==2:
            self.principle = args[0]
            self.rate = args[1]
        elif len(args)==3:
            self.principle = args[0]
            self.rate = args[1]
            self.time = args[2]
        elif len(args)==4:
            self.principle = args[0]
            self.rate = args[1]
            self.time = args[3]
            self.find_SI 
            

            interest = (self.principle*self.rate*self.time)/100
            print("The interest is {}".format(interest))

            net_change = self.principle + interest
            print("The net_change obtained is : {}".format(net_change))
            return net_change 
        
    def find_SI (self,rate): 
        self.time
        self.principle
        rate = rate
        SI = (self.time*self.principle*int(rate))/100
        print("The obtained simple interest is : {}".format(SI))
        print("The rate at which the amount provide : {}".format(rate))
        net_change = self.principle + SI
        print("The net change is {}",net_change)
        self.interest_rate = 0.05
        return SI
    
    def calculable(self): 
        self.find_SI(rate)

rate = input("Enter the rate")
bank = BankAccount(45645,45,4)








