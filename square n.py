N=int(input('Num:'))
import turtle
sq=turtle.Turtle()
def t():
    for r in range(N):
        for i in range(4):
            sq.fd(20)
            sq.rt(90)
            print(sq)
        sq.pu()
        sq.fd(40)
        sq.pd()
        for q in range(N):
            sq.bk(20*N)
            sq.lt(90)
    
        
t()
