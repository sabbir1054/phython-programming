class Account:
    def __init__(self,holder,initial_balance) -> None:
        self.holder=holder
        self.__balance=initial_balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def showBalance(self):
        return self.__balance

class StudentAccount(Account):
    def __init__(self, holder,initial_balance,school) -> None:
        self.school=school
        super().__init__(holder, initial_balance)
    def get_balance(self):
        return self.__balance

rafsan=StudentAccount("Rafsan",50000,"IUB")

print(rafsan.showBalance)
rafsan.deposit(2000)
# print(rafsan.balance)
rafsan.deposit(5000)
# print(rafsan.balance)
# rafsan.withdraw(1000)
# if i not encapsulated i can change from here example below
# rafsan.balance=100
# after encapsulation i cant change balance from here


# we can use single underscore to understand this thi protected
# print(rafsan._balance)