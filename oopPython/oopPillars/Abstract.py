from abc import ABC,abstractmethod                                        
class Animal(ABC):
   
    @abstractmethod
    def eat(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    # @name.setter
    # def name(self,value):
    #     self.__name=value
    @property
    def move(self):
        return "moving around the zoo"

class Monkey(Animal):
    def __init__(self) -> None:
        self.__name="monkey"
    def sing(self):
        print('Monkey is singing ')
    def eat(self):
        print("Monkey eat banana")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value


    

# abstract class abstract property

lyka=Monkey()

lyka.sing()
lyka.name="sagol"
print(lyka.name)