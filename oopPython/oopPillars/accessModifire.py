# public      |        protected                                       |           privet
# simple     | start with _(single underscore) its just an convention | for privet __(use double underscore)
class Account:
    pass


class StudentAccount(Account):
    def __init__(self,holder,balance,school) -> None:
        self.__balance=balance
        self._holder=holder #this is protected data

        self.school=school#public data
           
    def withdraw(self,amount):
        self.__balance-=amount

    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance



nas=StudentAccount("Nas Daily",12522,"Academy")
# nas.__balance=45656564654   its not working because this is privet
print(nas.get_balance())