import math
class triangle:
    def __init__(self, side1, side2, side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def check_type(self):
        if(self.side1==self.side2==self.side3):
            return 'Equilateral'
        elif(self.side1==self.side2!=self.side3 or self.side1==self.side3!=self.side2 or self.side2==self.side3!=self.side1):
            return 'isosceles'
        else:
            return'scalene'
    def area(self):
        a=(self.side1+self.side2+self.side3)/2
        ar=math.sqrt(a*(a-self.side1)*(a-self.side2)*(a-self.side3))
        return ar
    def __str__(self):
        return('The sides are %d, %d, %d, type is %s, area is %g' %(self.side1,self.side2,self.side3, self.check_type(), self.area()))
    def __lt__(self, self2):
        if(triangle.area(self)>triangle.area(self2)):
            return False
        elif(triangle.area(self)<triangle.area(self2) or triangle.area(self)==triangle.area(self2)):
            return True
        else:
            return False
            

t=triangle(3,4,5)
print(t)
t2=triangle(3,4,5)
print(t2)
print(triangle.area(t2))
print(triangle.area(t))
