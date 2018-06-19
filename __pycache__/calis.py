class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return('%d, %d' %(self.x, self.y))
    def __add__(self, n):
        self.x+=n
        self.y+=n
        return self
    def __radd__(self, n):
        return point.__add__(self, n)

class square:
    def __init__(self, x=0):
        self.side=x
    def __str__(self):
        return('The side of square is %d' %(self.side))
    def area(self):
        return ('Area: %d' %(self.side**2))

class cube(square):
    def area(self):
        return('The area of cube:%d' %(self.side**2*6))
    def volume(self):
        return('The volume of cube:%d' %(self.side**3))
class circle:
    def __init__(self, r=0, x=0, y=0):
        self.r=r
        self.center=point(x,y)
    def __str__(self):
        return('The radius is %d, the center is (%d, %d)' %(self.r, self.center.x, self.center.y))
    def __add__(self, n):
        self.r+=n
        return self
    def __radd__(self, n):
        return circle.__add__(self, n)

c=circle(2, 0, 1)
print(2+c)
s=cube(4)
print(cube.area(s))
print(cube.volume(s))
