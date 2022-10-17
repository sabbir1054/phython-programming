class Laptop:
    def __init__(self,brand,age):
        self.brand=brand
        self.age=age
    def increaseAge(self,age=1):
        self.age+=age
    def repair(self,life_increase=-5):
        self.increaseAge(life_increase)




my_laptop=Laptop('HP',1)
my_laptop.increaseAge()
my_laptop.age=50
my_laptop.increaseAge()
my_laptop.repair(-7)

print(my_laptop.age)
print(my_laptop.__dict__)