class Vehicle:
    def __init__(self,name,license,price) -> None:
        self.name=name
        self.license=license
        self.price=price
    def start(self):
        print(f'{self.name} started')

class Bus(Vehicle):
    def __init__(self, name, license, price,seat,ticket_price) -> None:
        super().__init__(name, license, price)
        self.seat=seat
        self.available_seat=seat
        self.ticket_price=ticket_price

    def sell_ticket(self,customer_name,quantity,amount):
        self.customer_name=customer_name
        self.available_seat-=quantity
        remainder=amount-self.ticket_price*quantity
        if remainder>=0:
            return Ticket(customer_name)
        else:
            return 'No ticket for you'
class AcBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        super().__init__(name, license, price, seat, ticket_price)
        pass

class MiniBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        super().__init__(name, license, price, seat, ticket_price)
        pass

class Ticket:
    def __init__(self,owner) -> None:
        self.owner=owner