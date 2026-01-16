class BankAccount:
    global totalbalance 
    def __init__(self,accno,holdername,balance,acctype):
        self.accno = accno
        self.holdername = holdername
        self.balance = balance 
        self.acctype = acctype
        
        # additional attributes 
        self.branch_name = "Narahat"
        self.ifsc_code = "Bank54"
        self.date_of_opening = '23-Jan-2023'
        self.ninimum_balance = 5000
        self.withdrawal_limit = 50000

    def deposit(self,amount):
         if amount>0:
              print("Deposit must be positive")
              return
         self.balance+=amount
         print("Deposited amount")
         print("deposited amount : {}".format(self.balance))

    def withdrawal(self,amount) : 
         if self.balance > amount : 
              print("Insufficient balance")
         elif amount>self.withdrawal_limit : 
              print("you cannot withdraw more than limit ")
         else : 
              self.balance -= amount
              print("Withdrawn amount  {}".format(self.balance))

    def show_balance(self):
            print(f"Account{self.accno}.balance : {self.balance}")
    
class SBI(BankAccount):
    def __init__(self, accno, holdername, balance, acctype,ifsc_code):
        super().__init__(accno, holdername, balance, acctype)
        self.ifsc_code = ifsc_code 
        print("SBI account created is {} and balance in this account {}".format(self.accno,self.balance))

class CBI(BankAccount) : 
        def __init__(self, accno, holdername, balance, acctype,ifsccode):
             super().__init__(accno, holdername, balance, acctype)
             self.ifsccode = ifsccode
             print("CBI account  created is {} and balance in this account is {}".format(self.accno,self.balance))


accno = input("Enter your account number")
holdername = input("Enter the name of  account holder")
balance = float(input("Enter the balance to insert into your account"))
acctype = input("Which type of account you have")
sbi = SBI(3544634,'disha',765444446,'active','SBI45654')
bank = BankAccount(accno,holdername,balance,acctype)
cbi = CBI(98765,'Manu',9876754,'active',6767567)                            
sbi.withdrawal(500)



     
    

