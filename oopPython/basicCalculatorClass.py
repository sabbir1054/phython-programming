class Calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        if a>b:
            print(a-b)
        else:
            print(b-a)
    def multiply(self,a,b):
        print(a*b)
    def divide(self,a,b):
        print(a/b)



casio=Calculator()
casio.add(41,85)
casio.sub(41,85)
casio.multiply(41,85)
casio.divide(41,85)
