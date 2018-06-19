import math
class triangle:
    def __init__(self, a=0, b=0, c=0):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        if(self.a==self.b==self.c):
            k='Equal'
        elif(self.a==self.b!=self.c or self.a==self.c!=self.b or self.b==self.c!=self.a):
            k='Isos'
        else:
            k='just'
        return('The sides are %d, %d, %d, triangle is %s' %(self.a,self.b,self.c,k))
    def area(self):
        p=(self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    def compare(self, self2):
        if(triangle.area(self)>triangle.area(self2)):
            return ('First is greater')
        if(triangle.area(self)<triangle.area(self2)):
            return ('First is less')
        else:
            return('There are equal')

t=triangle(3,4,5)
print(t)
t2=triangle(5,12,12)
print(t2)
print(triangle.compare(t, t2))
