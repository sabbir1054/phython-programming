from abc import ABC, abstractmethod


class Vehicle(ABC):
    speed={
        "car":30,
        "bike":50,
        "cng":15
    }
    def __init__(self,license_plate,vehicle_type,name,rate,driver) -> None:
        self.vehicle_type=vehicle_type
        self.rate=rate
        self.status="available"
        self.driver=driver
        self.license_plate=license_plate
        self.speed=self.speed[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, name, rate, driver) -> None:
        super().__init__(vehicle_type, name, rate, driver)

    def start_driving(self):
        self.status="unavailable"
        print(self.vehicle_type,"Started")
       
    def trip_finished(self):
        self.status="available"
        print(self.vehicle_type,self.license_plate,"complete trip")


class Bike(Vehicle):
    def __init__(self, vehicle_type, name, rate, driver) -> None:
        super().__init__(vehicle_type, name, rate, driver)

    def start_driving(self):
        self.status="unavailable"
        print(self.vehicle_type,"Started")
       
    def trip_finished(self):
        self.status="available"
        print(self.vehicle_type,self.license_plate,"complete trip")


class CNG(Vehicle):
    def __init__(self, vehicle_type, name, rate, driver) -> None:
        super().__init__(vehicle_type, name, rate, driver)

    def start_driving(self):
        self.status="unavailable"
        print(self.vehicle_type,"Started")
       
    def trip_finished(self):
        self.status="available"
        print(self.vehicle_type,self.license_plate,"complete trip")


