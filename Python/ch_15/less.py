class point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return("x: %d, y: %d" %(self.x, self.y))
    def __add__(self,n):
        self.x+=n
        self.y+=n
        return self
    def __radd__(self,n):
        return point.__add__(self,n)

p=point(4,3)
print(p)
print(p+10)
5+p
print(p)

p2=point(6,7)
print(p2)

class circle:
    def __int__(self, r, x, y):
        self.rad=r
        self.center=point(x,y)
    def __str__(self):
        return ("r: %d, center at(%d,%d)" %(self.rad, self.center.x, self.center.y))

c=circle(10, 2, 4)
print(c)
