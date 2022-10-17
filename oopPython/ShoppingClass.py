from unicodedata import name


class Shopper:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    
    def add_to_cart(self,item,price,quantity):
        self.cart.append({'item':item,'price':price,'quantity':quantity})

    def checkout(self,amount):
        #  print(self.cart)
        price=0
        for item in self.cart:
            price=price+item['price']* item['quantity']
            print(item)
        if amount<price:
            return f'Please give me more {price-amount} tk'
        elif amount==price:
            return 'Thank you '
        else:
            return f'Take this {amount-price} tk'

    

shopping =Shopper('Jihad')
shopping.add_to_cart('Shirt',1000,2)
shopping.add_to_cart('Pen',10,3)
shopping.add_to_cart('Khata',60,8)

print(shopping.checkout(2510))