class SumAndPow:
    def __init__(self,X,n) -> None:
        self.X=X
        self.n=n
    def sum(self):
        return self.X+self.n
    def pow(self):
        return pow(self.X,self.n)
print(f"Sum={SumAndPow(2,4).sum()} and Power = {SumAndPow(2,4).pow()}")

