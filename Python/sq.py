class square:
    def __init__(self, x=0):
        self.si=x
    def __str___(self):
        return("Side: %d" %(self.si))
    def audan(self):
        return self.si*self.si
    def perimeter(self):
        return self.si*4
    def com(a1, a2):
        if(a1.si<a2.si):
            print('Second is bigger')
        elif(a1.si>a2.si):
            print('First is bigger')
        elif(a1.si==a2.si):
            print('They are equal')
        else:
            print('Error0')
    def __lt__(a1,a2):
        if(a1.si<a2.si):
            return True
        if(a1.si>a2.si):
            return False

class cube(square):
    def area(self):
        return self.si*self.si*6
    def volume(self):
        return self.si**3

c=cube(4)
print(cube.area(c))
c2=cube(5)
print(cube.area(c2))
