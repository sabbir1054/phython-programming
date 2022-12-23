import random
class BRTA:
    def __init__(self) -> None:
        self.__licenses={}

    def driving_test(self,email):
        score=random.randint(0,100)
        if score>=33:
            print("Congrats...",score);
            license_number=random.randint(5000,9999)
            self.__licenses[email]=license_number
            return license_number
        else:
            print("sorry....",score)
            return False
        
    def validate_license(self,email,license):
        for key, value in self.__licenses.items():
            if key==email and value == license:
                return True
            else:
                return False

