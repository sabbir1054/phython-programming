class Account:
    def __init__(self,holder,age,nid,mobile,balance) -> None:
        self.name=holder
        self.age=age
        self.nid=nid
        self.mobile=mobile
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance+=amount
    

account1=Account("Sabbir",20,77878687,+8801733208221,200)
account2=Account("Zihad",22,255458,5978897,14444444,12577)
account1.deposit(300)
print(account1.balance)
    
