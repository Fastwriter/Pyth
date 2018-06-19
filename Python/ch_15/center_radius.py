class circle:
    def __int__(self, r, x, y):
        self.rad=r
        self.center=point(x,y)
    def __str__(self):
        return ("r: %d, center at(%d,%d)" %(self.rad, self.center.x, self.center.y))
c=circle(10, 2, 4)
print(c)

