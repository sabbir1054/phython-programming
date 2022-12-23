""" overloading """


# this are method overloading
# normal function
def add(num1,num2):
    return num1+num2

# we give it overload
# print(4,5,6)
# create overload
def add2(num1,num2,num3=0,num4=0):
    return num1+num2+num3+num4

# another overloading function
def add3(*args,**Kwargs):
    pass

# operator overloading
print(12+13)

# the example of our custom overload

class Account:
    def __init__(self,holder,balance) -> None:
        self.holder=holder
        self.__balance=balance
    # make overload
    def __add__(self,other):
        return self.__balance+other.__balance


my_account=Account("Shakib al hasan",5000)
her_account=Account("Sisir",44554)

result=my_account+her_account
print(result)