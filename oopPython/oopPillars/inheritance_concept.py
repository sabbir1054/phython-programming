# parent class
# base class
class BaseClass:
    pass

# derived class
# child class
class DerivedClass(BaseClass):
    pass


class Device:
    def __init__(self,brand,price,color) -> None:
        self.brand=brand
        self.price=price
        self.color=color
    def re_sale(self):
        print("Ready to sale")


class Laptop(Device):
    def __init__(self,brand,price,color,desc) -> None:
        super().__init__(brand,price,color)
        self.desc=desc

    def run(self):
        print("Running the laptop")

    def purchase(self,money):
        if money<self.price:
            return 'No laptop for you'
        else:
            print("this device is for you")
            return money-self.price
    def __repr__(self) -> str:
        return f'This is {self.brand} laptop price {self.price} color: {self.color}'

class Phone(Device):
    def __init__(self,brand,price,color,camera,sim_number) -> None:
        super().__init__(brand,price,color)
        self.camera=camera
        self.sim_number=sim_number
    
    def is_dual_sim(self):
        return self.sim_number>1
    def __repr__(self) -> str:
        return f'This is {self.brand} phone price {self.price} color: {self.color}'

class Watch:
    def __init__(self,brand,price,color,watchType) -> None:
        self.brand=brand
        self,price=price
        self.color=color
        self.watchType=watchType
    
    def is_digital(self):
        return self.watchType=='Digital'



class Manager:
    def __init__(self,name,salary,experience,designation) -> None:
        pass
    
    def day_total_sales(self):
        pass
    def handle_customers_complain(self):
        pass

class SalesMan:
    def __init__(self,name,salary,experience,designation,commission) -> None:
        pass



lenevo=Laptop("Lenevo",42000,'Black',"500gb")
hp=Laptop("HP",42000,'Silver',"500gb")

oppo=Phone("Oppo",1500,'Black',"15Mgpxl",1)
sumsung=Phone("Sumsung",15000,'Black',"13Mgpxl",2)


print(lenevo)
print(hp)
print(oppo)
print(sumsung)