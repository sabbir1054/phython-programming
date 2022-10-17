class Bank:
    def __init__(self,balance) -> None:
        self.balance=balance
        self.minimum_withdraw=100
        self.max_withdraw=10000
        self.min_deposit=100
    
    def get_balance(self):
        return f'Your balance is {self.balance}'
    
    def withdraw(self,amount):
        if(amount<self.minimum_withdraw):
            return f'Minimum withdraw is = {self.minimum_withdraw}'
        elif(amount>self.max_withdraw ):
            return f'Maximum withdraw limit is = {self.max_withdraw}'
        elif(amount>self.balance):
            return f'You have not enough balance'
        else:
            self.balance-=amount
            return f'Take your money = {amount}'
    def deposit(self,amount):
        if(amount<self.min_deposit):
            return f'Minimum amount of deposit is = {self.min_deposit}'
        else:
            self.balance+=amount
            return f'Deposit successful.'

bank_asia=Bank(150)

replay=bank_asia.withdraw(500)
print(replay)
print(bank_asia.get_balance())

replay2=bank_asia.deposit(10000)
print(replay2)
print(bank_asia.get_balance())

replay3=bank_asia.withdraw(500)
print(replay3)
print(bank_asia.get_balance())