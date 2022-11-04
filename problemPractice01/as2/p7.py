class Subsets:
    def getSub(self, s):
        return self.subsets([], sorted(s))
   
    def subsets(self, current, s):
        if s:
            return self.subsets(current, s[1:]) + self.subsets(current + [s[0]], s[1:])
        return [current]
 
print(Subsets().getSub([4,5,6]))