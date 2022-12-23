""" Polymorphism is the concept that we can use same thing s in different way """
""" Here is the main discussion on  method overriding"""
class Animal:
    def __init__(self,name) -> None:
        self.name=name
    def make_sound(self):
        print("Animal making sound")

class Cat (Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("mewo mewo")

class  Dog(Animal):
    def __init__(self, name) -> None:
        # super().__init__(name)
        Animal.__init__(self,name)# we can also use by this way
    def make_sound(self):
        print("Bark Bark")
        
class Horse(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print("Ney ney")

don=Cat('don')
don.make_sound()

shepard=Dog("garman Shepard")
shepard.make_sound()

kalaManik=Horse("KalaManik")
kalaManik.make_sound()

""" We can also use this method """
print("---------------------------")
animals=[don,shepard,kalaManik]

for animal in animals:
    animal.make_sound()