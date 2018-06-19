class point:
    x=0.0
    y=0.0
    
class rect:
    w=0.0
    h=0.0
    z=point()
    
class circle:
    c=point()
    r=0.0

p=point()    
p.x=150.0
p.y=100.0
c=circle()
c.c.x=5
c.c.y=5
c.r=75.0
a=point()
a.x=3
a.y=4
b=point()
b.x=7
b.y=10
r=rect()
r.z.x=10
r.z.y=10
r.h=10
r.w=10
def center(rect):
    p=point()
    p.x=rect.p.x + rect.w/2
    p.y=rect.p.y + rect.h/2
    return p
def point_in_circle(point,circle):
    dist_from_centre_in_square=(circle.c.x-point.x)**2+(circle.c.y-point.y)**2
    if dist_from_centre_in_square<=circle.r**2:
        return True
    else:
        return False
def rect_in_circle(rect,circle):
    a=point_in_circle(rect.z,circle)
    d=point()
    d.x=rect.z.x+rect.w
    d.y=rect.z.y-rect.h
    b=point_in_circle(d,circle)
    if a and b is True:
        return True
    else:
        return False
