class User:
    def __init__(self,name,password,phone):
        self.name=name
        self.__password=password
        self.__phone=phone
    def __get_pass(self):
        print(self.__password)

ryan=User('Ryan',"fsdfsd","014587456")
# print(ryan.__password)

ryan.__get_pass()