class Person:
    def __init__(self,name,age,money):
        self.name=name
        self.age=age
        self.money=money
    def __eq__(self,others):
        return self.age==others.age
    def __call__(self):
        print(f'THis is {self.name}')
    
    def __add__(self,other):
        return self.money+other.money

alim = Person('Alim',15,560)
dalim = Person('Dalim',15,560)

alim()

print(alim+ dalim)
print(alim==dalim)

""" 

10 20 10 40 50 60 70 """