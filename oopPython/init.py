class Phone:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color

    def send_sms(self,number,text):
        sms=f'sending : {'