import math


class Distance:
    def __init__(self,x1,y1,x2,y2):
        self._x = x1
        self._y = y1
        self.x= x2
        self.y = y2
    def findDistance(self):
        result =math.sqrt(pow((self.x-self._x),2)+pow((self.y-self._y),2))
        return result
   
result = Distance(3,2,7,3)
print(result.findDistance())
