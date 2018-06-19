class point:
    x=0.0
    y=0.0
        
class rect():
    w=0.0
    h=0.0
    p=point()

r=rect()    
r.w=80.0
r.h=40.0
r.p.x=0.0
r.p.y=0.0

def center(rect):
    p=point()
    p.x=rect.p.x + rect.w/2
    p.y=rect.p.y + rect.h/2
    return p
