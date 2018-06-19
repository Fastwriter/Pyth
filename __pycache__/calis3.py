import turtle
s=turtle.Turtle()

class point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return ('%d, %d' %(self.x, self.y))
class rect:
    def __init__(self, h=0, w=0, x=0, y=0):
        self.h=h
        self.w=w
        self.corner=point(x, y)
    def __str__(self):
        return('H: %d, W: $d' %(self.h, self.w))
    def draw(self, t):
        t.pu()
        t.goto(self.corner.x, self.corner.y)
        t.pd()
        for i in range(2):
            t.fd(self.w)
            t.rt(90)
            t.fd(self.h)
            t.rt(90)


r=rect(100, 200, 50, 100)
rect.draw(r, s)
