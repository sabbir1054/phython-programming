class Laptop:
    def __init__(self,brand,price,color,desc) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.desc=desc

    def run(self):
        print("Running the laptop")

    def purchase(self,money):
        if money<self.price:
            return 'No laptop for you'
        else:
            print("this device is for you")
            return money-self.price


class Phone:
    def __init__(self,brand,price,color,camera,sim_number) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.camera=camera
        self.sim_number=sim_number
    
    def is_dual_sim(self):
        return self.sim_number>1
    

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