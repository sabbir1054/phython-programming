import hashlib
from random import randint
from brta import BRTA
from vhicles import Bike, Car
from ridemanager import uber


license_authority=BRTA()

class User:
    def __init__(self,name,email,password) -> None:
        self.name=name 
        self.email=email
        self.password=password
        encrypted_pwd=hashlib.md5((self.password).encode()).hexdigest()
        with open('user.txt',"a+")as f:
            f.write(f'{email} {encrypted_pwd}\n')
        f.close()
        print(self.name,'User created successfully')
    
    @staticmethod
    def login(email,password):
        with open('user.txt','r')as f:
            lines=f.readlines()
            for line in lines:
                if email in line:
                    
                    _,stored_password=line.split(' ')
        f.close()
        hashed_pass=hashlib.md5(password.encode()).hexdigest()
        if hashed_pass== stored_password:
            print("valid user")
        else:
            "Invalid user"
        # print("password found ",stored_password)


class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        self.location=location
        self.balance=balance
        super().__init__(name, email, password)

    def set_location(self,location):
        self.location=location
    def get_location(self):
        return self.location
    def req_trip(self,destination):
        pass
    def start_trip(self,fare):
        self.balance-=fare

class Driver(User):
    def __init__(self, name, email, password,location,license,balance) -> None:

        super().__init__(name, email, password)

        self.location=location
        self.license=license
        self.valid_driver=license_authority.validate_license(email,license)
        self.earning=0

    def register_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            new_vehicle=None;
            if vehicle_type=="car":
                new_vehicle=Car(vehicle_type,license_plate,rate,self.email)
            elif vehicle_type=="bike":
                new_vehicle=Bike(vehicle_type,license_plate,rate,self.email)
            else:
                new_vehicle=Bike(vehicle_type,license_plate,rate,self.email)
        else:
            print("You are not a valid driver")

    def take_driving_test(self):
        result = license_authority.driving_test(self.email)
        if result==False:
            print("sorry you are fail ")
        else:
            self.license=result
            self.valid_driver=True

    def start_trip(self,destination,fare):
        self.earning+=fare
        self.location=destination
        
""" 


hero=User("sabbir","sabbir.com","sabbir1054")

User.login("sabbir.com","sabbir10504")

kuber=Driver("Kuber Maji","Kuber@gmail","vsdf645","uttara",54,52)

result =license_authority.validate_license(kuber.email,kuber.license)
print(result)
kuber.take_driving_test()
result2 =license_authority.validate_license(kuber.email,kuber.license)
print(result2) """

rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1', randint(0, 30), 5000)
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2', randint(0, 30), 5000)
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3', randint(0, 30), 5000)

driver1 = Driver('driver1', 'driver1@gmail.com', 'driver1',"mirpur", randint(0, 30), 5645)
driver1.take_driving_test()
driver1.register_vehicle('car', 1245, 10)

driver2 = Driver('driver2', 'driver2@gmail.com', 'driver2',"dhaka", randint(0, 30), 5645)
driver2.take_driving_test()
driver2.register_vehicle('car', 1245, 10)

driver3 = Driver('driver3', 'driver3@gmail.com', 'driver3',"shantinagar", randint(0, 30), 5645)
driver3.take_driving_test()
driver3.register_vehicle('car', 2145, 10)

driver4 = Driver('driver4', 'driver4@gmail.com', 'driver4',"savar", randint(0, 30), 5645)
driver4.take_driving_test()
driver4.register_vehicle('car', 3245, 10)

print(uber.get_available_cars())
uber.find_vehicle(rider1, 'car', 90)