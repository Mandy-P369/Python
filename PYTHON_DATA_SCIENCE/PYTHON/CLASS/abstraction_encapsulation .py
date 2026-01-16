# Abstraction : 
# Hiding the implementation of the class and only showing the essential features to the user...

# Encapsulation : 
# Wrapping data and function into the single unit(object).
class Account : 
    def __init__(self,bal,accno ):
        self.accountnumber = accno
        self.balance = bal
    
    def debit(self,amount):
        self.balance-=amount
        print("The amount {}".format(amount),'debitted from your account {}'.format(self.accountnumber))
        new_balance =self.balance
        print("New balance obtained is : {}".format(new_balance))
        return new_balance

    def credit(self,amount):
        self.balance +=amount
        print("The amount {}".format(amount),"added into accountnumber {}".format(self.accountnumber))
        new_balance = self.balance
        print("Now your amount in your bank account {} is {}".format(self.accountnumber,new_balance))
        return new_balance


initialbalance = int(input("Enter the balance inside the account"))
accno = input("Enter your account number")
account1 = Account(initialbalance,accno)

key=1
while key!=3:
    print("Enter the key 1 to debit from the balance ")
    print("Enter the key 2 to credit inside the balance")
    key = int(input("Enter the key"))
    if(key==1):
        amount = int(input("Enter  the amount you want to withdraaw from the account"))
        account1.debit(amount)
    elif(key==2):
        amount = int(input("Enter the amount you want to insert inside the account"))
        account1.credit(amount)
       
    
    





        